import unittest
from platform import python_version

from algoliasearch.user_agent import UserAgent
from algoliasearch.version import VERSION


class TestUserAgent(unittest.TestCase):
    default = 'Algolia for Python ({}); Python ({})'.format(
        VERSION, str(python_version()))

    def tearDown(self):
        UserAgent.value = str(TestUserAgent.default)

    def test_default_value(self):
        self.assertEqual(UserAgent.get(), TestUserAgent.default)

    def test_add(self):
        UserAgent.add('Foo Bar', 'v1.0')
        UserAgent.add('Front Web', '2.0')

        self.assertEqual(
            UserAgent.get(),
            '{}; Foo Bar (v1.0); Front Web (2.0)'.format(TestUserAgent.default)
        )
