import unittest

from tests.helpers.env import Env
from tests.helpers.factory import Factory as F


class TestRecommendationClient(unittest.TestCase):
    def setUp(self):
        self.client = F.recommendation_client()

    @unittest.skipIf(Env.is_community(),
                     "Community can not test personalization operations")
    def test_recommendation(self):
        personalization_strategy = {
            'eventsScoring': [
                {
                    'eventName': 'Add to cart',
                    'eventType': 'conversion',
                    'score': 50
                },
                {
                    'eventName': 'Purchase',
                    'eventType': 'conversion',
                    'score': 100
                },
            ],
            'facetsScoring': [
                {'facetName': 'brand', 'score': 100},
                {'facetName': 'categories', 'score': 10},
            ],
            'personalizationImpact': 0,
        }

        response = self.client.set_personalization_strategy(
            personalization_strategy
        )

        self.assertEqual(response, {
            'status': 200,
            'message': 'Strategy was successfully updated'
        })

        response = self.client.get_personalization_strategy()
        self.assertEqual(response, personalization_strategy)
