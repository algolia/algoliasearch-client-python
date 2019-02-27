import asyncio

from algoliasearch.exceptions import RequestException, \
    AlgoliaUnreachableHostException
from algoliasearch.http.transporter import Transporter as Base, RetryOutcome


class TransporterAsync(Base):

    @asyncio.coroutine
    def retry(self, hosts, request, relative_url):
        for host in hosts:

            request.url = 'https://%s/%s' % (
                host.url, relative_url)

            response = yield from self._requester.send(request)

            decision = self._retry_strategy.decide(host, response)

            if decision == RetryOutcome.SUCCESS:
                return response.content if response.content is not None else {}
            elif decision == RetryOutcome.FAIL:
                content = response.error_message
                if response.content and 'message' in response.content:
                    content = response.content['message']

                raise RequestException(content, response.status_code)

        raise AlgoliaUnreachableHostException('Unreachable hosts')
