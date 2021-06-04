import unittest

from algoliasearch.exceptions import RequestException
from tests.helpers.factory import Factory as F


class TestAnswersClient(unittest.TestCase):
    def setUp(self):
        self.search_client = F.search_client()
        self.client = F.answers_client()
        self.index = F.index(self.search_client, self._testMethodName)
        self.index.save_objects(
            [
                {
                    "name": "Something",
                    "description": "Your usage of demo datasets is usually more creative :')",
                    "objectID": 0,
                },
                {
                    "name": "Another thing",
                    "description": "This is creative, but unused. ;)",
                    "objectID": 1,
                },
            ]
        ).wait()

    def tearDown(self):
        self.client.close()

    def test_answers(self):
        data = {
            "query": "Any usage?",
            "queryLanguages": ["en"],
            "attributesForPrediction": ["title", "description"],
            "nbHits": 2,
        }

        try:
            response = self.client.predict(self.index.name, data)
            print(response)
            self.assertTrue("hits" in response)
            self.assertIn("usage", response["hits"][0]["_answer"]["extract"])
            self.assertEqual("0", response["hits"][0]["objectID"])
        except RequestException as err:
            self.fail(err)  # noqa: E501
