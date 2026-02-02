import asyncio
import time
from os import environ
from typing import Tuple

from algoliasearch.http.base_config import BaseConfig
from algoliasearch.http.hosts import CallType, Host, HostsCollection
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.transporter import Transporter
from algoliasearch.http.transporter_sync import TransporterSync
from algoliasearch.http.verb import Verb

TEST_SERVER = (
    "localhost" if environ.get("CI") == "true" else "host.docker.internal"
) + ":6676"


def create_config_with_host(host_url: str) -> Tuple[BaseConfig, Host]:
    config = BaseConfig("test-app", "test-key")
    host = Host(host_url, accept=CallType.READ | CallType.WRITE)
    config.hosts = HostsCollection([host])
    return config, host


def create_server_host() -> Host:
    return Host(TEST_SERVER, scheme="http", accept=CallType.READ | CallType.WRITE)


def test_sync_retry_count_stateful():
    """connect timeout increases across failed requests: 2s -> 4s -> 6s."""
    config, _ = create_config_with_host("10.255.255.1")
    transporter = TransporterSync(config)
    request_options = RequestOptions(config).merge()

    times = []
    for _ in range(3):
        start = time.time()
        try:
            transporter.request(
                verb=Verb.GET,
                path="/test",
                request_options=request_options,
                use_read_transporter=True,
            )
        except Exception:
            times.append(time.time() - start)

    assert 1.5 < times[0] < 2.5, f"Request 1 should be ~2s, got {times[0]:.2f}s"
    assert 3.5 < times[1] < 4.5, f"Request 2 should be ~4s, got {times[1]:.2f}s"
    assert 5.5 < times[2] < 7.5, f"Request 3 should be ~6s, got {times[2]:.2f}s"


def test_sync_retry_count_resets():
    """retry_count resets to 0 after successful request."""
    config, bad_host = create_config_with_host("10.255.255.1")
    good_host = create_server_host()

    transporter = TransporterSync(config)
    request_options = RequestOptions(config).merge()

    # fail twice to increment retry_count
    for _ in range(2):
        try:
            transporter.request(
                verb=Verb.GET,
                path="/test",
                request_options=request_options,
                use_read_transporter=True,
            )
        except Exception:
            pass

    # switch to good host and succeed
    config.hosts = HostsCollection([good_host])
    transporter._hosts = [good_host]
    good_host.retry_count = bad_host.retry_count

    response = transporter.request(
        verb=Verb.GET,
        path="/1/test/instant",
        request_options=request_options,
        use_read_transporter=True,
    )
    assert response.status_code == 200
    assert good_host.retry_count == 0, (
        f"retry_count should reset to 0, got {good_host.retry_count}"
    )

    # point to bad host again, should timeout at 2s (not 6s)
    good_host.url = "10.255.255.1"
    good_host.scheme = "https"

    start = time.time()
    try:
        transporter.request(
            verb=Verb.GET,
            path="/test",
            request_options=request_options,
            use_read_transporter=True,
        )
        assert False, "Request should have timed out"
    except Exception:
        elapsed = time.time() - start
        assert 1.5 < elapsed < 2.5, f"After reset should be ~2s, got {elapsed:.2f}s"


async def test_async_retry_count_stateful():
    """async connect timeout increases across failed requests: 2s -> 4s -> 6s."""
    config, _ = create_config_with_host("10.255.255.1")
    transporter = Transporter(config)
    request_options = RequestOptions(config).merge()

    times = []
    for _ in range(3):
        start = time.time()
        try:
            await transporter.request(
                verb=Verb.GET,
                path="/test",
                request_options=request_options,
                use_read_transporter=True,
            )
        except Exception:
            times.append(time.time() - start)

    await transporter.close()

    assert 1.5 < times[0] < 2.5, f"Request 1 should be ~2s, got {times[0]:.2f}s"
    assert 3.5 < times[1] < 4.5, f"Request 2 should be ~4s, got {times[1]:.2f}s"
    assert 5.5 < times[2] < 7.5, f"Request 3 should be ~6s, got {times[2]:.2f}s"


async def test_async_retry_count_resets():
    """async retry_count resets to 0 after successful request."""
    config, bad_host = create_config_with_host("10.255.255.1")
    good_host = create_server_host()

    transporter = Transporter(config)
    request_options = RequestOptions(config).merge()

    # fail twice to increment retry_count
    for _ in range(2):
        try:
            await transporter.request(
                verb=Verb.GET,
                path="/test",
                request_options=request_options,
                use_read_transporter=True,
            )
        except Exception:
            pass

    # switch to good host and succeed
    config.hosts = HostsCollection([good_host])
    transporter._hosts = [good_host]
    good_host.retry_count = bad_host.retry_count

    response = await transporter.request(
        verb=Verb.GET,
        path="/1/test/instant",
        request_options=request_options,
        use_read_transporter=True,
    )
    assert response.status_code == 200
    assert good_host.retry_count == 0, (
        f"retry_count should reset to 0, got {good_host.retry_count}"
    )

    # point to bad host again, should timeout at 2s (not 6s)
    good_host.url = "10.255.255.1"
    good_host.scheme = "https"

    start = time.time()
    try:
        await transporter.request(
            verb=Verb.GET,
            path="/test",
            request_options=request_options,
            use_read_transporter=True,
        )
        assert False, "Request should have timed out"
    except Exception:
        elapsed = time.time() - start
        assert 1.5 < elapsed < 2.5, f"After reset should be ~2s, got {elapsed:.2f}s"
    finally:
        await transporter.close()


# pytest integration for async tests
def test_async_retry_count_stateful_sync():
    asyncio.run(test_async_retry_count_stateful())


def test_async_retry_count_resets_sync():
    asyncio.run(test_async_retry_count_resets())
