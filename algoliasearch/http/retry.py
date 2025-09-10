import time
from typing import List

from algoliasearch.http.api_response import ApiResponse
from algoliasearch.http.hosts import Host


class RetryOutcome:
    SUCCESS = "SUCCESS"
    RETRY = "RETRY"
    FAIL = "FAIL"


class RetryStrategy:
    def valid_hosts(self, hosts: List[Host]) -> List[Host]:
        for host in hosts:
            if not host.up and time.time() - host.last_use > Host.TTL:
                host.up = True

        return [host for host in hosts if host.up]

    def _now(self) -> float:
        return time.time()

    def decide(self, host: Host, response: ApiResponse) -> str:
        host.last_use = time.time()

        if response.is_timed_out_error:
            host.retry_count += 1

            return RetryOutcome.RETRY
        elif self._is_retryable(response):
            host.up = False

            return RetryOutcome.RETRY
        elif self._is_success(response):
            return RetryOutcome.SUCCESS

        return RetryOutcome.FAIL

    def _is_success(self, response: ApiResponse) -> bool:
        return response.status_code is not None and (response.status_code // 100) == 2

    def _is_retryable(self, response: ApiResponse) -> bool:
        if response.is_network_error:
            return True

        return (
            response.status_code is not None
            and (response.status_code // 100) != 2
            and (response.status_code // 100) != 4
        )
