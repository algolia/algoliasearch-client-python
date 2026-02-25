from typing import Any, Dict, Optional, Union

from requests import PreparedRequest, Request, Response, Session
from requests.structures import CaseInsensitiveDict

from algoliasearch.http.base_config import BaseConfig
from algoliasearch.http.hosts import CallType, Host, HostsCollection
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.transporter_sync import TransporterSync
from algoliasearch.http.verb import Verb


class FakeResponse(Response):
    def __init__(self, body_text: str) -> None:
        super().__init__()
        self.status_code = 200
        self.headers = CaseInsensitiveDict()
        self.reason = "OK"
        self._body_text = body_text

    @property
    def text(self) -> str:
        return self._body_text


class FakeSession(Session):
    def __init__(self, response: FakeResponse) -> None:
        super().__init__()
        self._response = response
        self.prepare_request_calls = 0
        self.prepared_input: Optional[Request] = None
        self.prepared_request = PreparedRequest()
        self.send_input: Optional[PreparedRequest] = None

    def prepare_request(self, request: Request) -> PreparedRequest:
        self.prepare_request_calls += 1
        self.prepared_input = request
        self.prepared_request = super().prepare_request(request)
        return self.prepared_request

    def send(
        self,
        request: PreparedRequest,
        verify: Union[bool, str] = True,
        stream: bool = False,
        cert: Optional[Union[str, tuple]] = None,
        proxies: Optional[Dict[str, str]] = None,
        timeout: Optional[Union[float, tuple]] = None,
        allow_redirects: bool = True,
        **kwargs: Any,
    ) -> Response:
        _ = stream
        _ = timeout
        _ = verify
        _ = cert
        _ = proxies
        _ = allow_redirects
        _ = kwargs
        self.send_input = request
        return self._response


def create_config() -> BaseConfig:
    config = BaseConfig("test-app", "test-key")
    config.hosts = HostsCollection(
        [Host("localhost", accept=CallType.READ | CallType.WRITE)]
    )
    return config


def test_sync_transporter_uses_session_prepare_request_and_sends_gzip() -> None:
    config = create_config()
    transporter = TransporterSync(config)
    fake_response = FakeResponse('{"ok":true}')
    fake_session = FakeSession(fake_response)
    transporter._session = fake_session

    response = transporter.request(
        verb=Verb.GET,
        path="/test",
        request_options=RequestOptions(config).merge(),
        use_read_transporter=True,
    )

    assert fake_session.prepare_request_calls == 1
    assert isinstance(fake_session.prepared_input, Request)
    assert fake_session.prepared_input.method in (Verb.GET, "GET")
    assert fake_session.send_input is fake_session.prepared_request
    assert fake_session.send_input is not None
    accept_encoding = fake_session.send_input.headers.get("Accept-Encoding")
    assert accept_encoding is not None
    assert "gzip" in accept_encoding.lower()
    assert response.status_code == 200
