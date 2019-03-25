import unittest

from algoliasearch.account_client import AccountClient
from algoliasearch.exceptions import AlgoliaException
from tests.helpers.factory import Factory as F


class TestAccountClient(unittest.TestCase):
    def test_can_not_copy_index_from_same_account(self):
        index1 = F.index('foo')
        index2 = F.index('bar')

        # Assert that copying indexes of same application
        with self.assertRaises(AlgoliaException) as _:
            AccountClient.copy_index(index1, index2)
