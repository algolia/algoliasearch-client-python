from algoliasearch.configs import SearchConfig
from algoliasearch.helpers_async import _create_async_methods_in
from algoliasearch.http.transporter import Transporter
from algoliasearch.insights_client import InsightsClient, UserInsightsClient


class InsightsClientAsync(InsightsClient):

    def __init__(self, insights_client, transporter, search_config):
        # type: (InsightsClient, Transporter, SearchConfig) -> None

        super(InsightsClientAsync, self).__init__(insights_client._transporter,
                                                  search_config)

        client = InsightsClient(transporter, search_config)

        _create_async_methods_in(self, client)

    def user(self, user_token):
        # type: (str) -> UserInsightsClient

        return UserInsightsClientAsync(self, user_token)


class UserInsightsClientAsync(UserInsightsClient):

    def __init__(self, insights_client, user_token):
        # type: (InsightsClient, Transporter, SearchConfig) -> None

        super(UserInsightsClientAsync, self).__init__(
            insights_client,
            user_token
        )

        client = UserInsightsClient(insights_client, user_token)

        _create_async_methods_in(self, client)
