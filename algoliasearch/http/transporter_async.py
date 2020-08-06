import asyncio

from algoliasearch.configs import Config
from algoliasearch.exceptions import RequestException, AlgoliaUnreachableHostException
from algoliasearch.http.hosts import HostsCollection
from algoliasearch.http.requester_async import RequesterAsync
from algoliasearch.http.transporter import (
    Transporter,
    RetryOutcome,
    Request,
    RetryStrategy,
)


class TransporterAsync(Transporter):
    @asyncio.coroutine
    def retry(self, hosts, request, relative_url):  # type: ignore
        # type: (list, Request, str) -> dict

        for host in self._retry_strategy.valid_hosts(hosts):

            request.url = "https://{}/{}".format(host.url, relative_url)

            response = yield from self._requester.send(request)  # type: ignore

            decision = self._retry_strategy.decide(host, response)

            if decision == RetryOutcome.SUCCESS:

                return response.content if response.content is not None else {}
            elif decision == RetryOutcome.FAIL:
                content = response.error_message
                if response.content and "message" in response.content:
                    content = response.content["message"]

                raise RequestException(content, response.status_code)

        raise AlgoliaUnreachableHostException("Unreachable hosts")

    @asyncio.coroutine
    def close(self):  # type: ignore
        # type: () -> None

        yield from self._requester.close()  # type: ignore
