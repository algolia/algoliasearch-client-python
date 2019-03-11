from algoliasearch.configs import InsightsConfig, InsightsConfig
from algoliasearch.helpers_async import _create_async_methods_in
from algoliasearch.http.transporter import Transporter
from algoliasearch.insights_client import InsightsClient, UserInsightsClient


class InsightsClientAsync(InsightsClient):

    def __init__(self, insights_client, transporter, insights_config):
        # type: (InsightsClient, Transporter, InsightsConfig) -> None

        super(InsightsClientAsync, self).__init__(insights_client._transporter,
                                                  insights_config)

        client = InsightsClient(transporter, insights_config)

        _create_async_methods_in(self, client)

    def user(self, user_token):
        # type: (str) -> UserInsightsClientAsync

        return UserInsightsClientAsync(self, user_token)


class UserInsightsClientAsync(UserInsightsClient):

    def __init__(self, insights_client, user_token):
        # type: (InsightsClient, Transporter, InsightsConfig) -> None

        super(UserInsightsClientAsync, self).__init__(
            insights_client._transporter,
            user_token
        )

        client = UserInsightsClient(insights_client, user_token)

        _create_async_methods_in(self, client)
