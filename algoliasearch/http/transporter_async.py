from algoliasearch.configs import Config
from algoliasearch.exceptions import AlgoliaUnreachableHostException, RequestException
from algoliasearch.http.hosts import HostsCollection
from algoliasearch.http.requester_async import RequesterAsync
from algoliasearch.http.transporter import (
    Request,
    RetryOutcome,
    RetryStrategy,
    Transporter,
)


class TransporterAsync(Transporter):
    async def retry(self, hosts, request, relative_url):  # type: ignore
        # type: (list, Request, str) -> dict

        for host in self._retry_strategy.valid_hosts(hosts):
            request.url = "https://{}/{}".format(host.url, relative_url)

            response = await self._requester.send(request)  # type: ignore

            decision = self._retry_strategy.decide(host, response)

            if decision == RetryOutcome.SUCCESS:
                return response.content if response.content is not None else {}
            elif decision == RetryOutcome.FAIL:
                content = response.error_message
                if response.content and "message" in response.content:
                    content = response.content["message"]

                raise RequestException(content, response.status_code)

        raise AlgoliaUnreachableHostException("Unreachable hosts")

    async def close(self):  # type: ignore
        # type: () -> None

        await self._requester.close()  # type: ignore
