import time
import unittest
import mock as mock

from algoliasearch.configs import SearchConfig
from algoliasearch.exceptions import AlgoliaUnreachableHostException, \
    AlgoliaException
from algoliasearch.http.hosts import Host
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.requester import Requester
from algoliasearch.http.transporter import Transporter, Response, \
    RetryStrategy, RetryOutcome


class TestTransporter(unittest.TestCase):
    def setUp(self):
        self.requester = Requester()
        self.requester.request = mock.Mock(name="request")
        self.requester.request.return_value = Response(200, {'foo': 'bar'})

        self.data = {
            'data': 'foo'
        }

        self.config = SearchConfig('foo', 'bar')

        self.request_options = RequestOptions.create(self.config, {
            'User-Agent': 'foo',
            'createIfNotExists': True,
            'readTimeout': 109,
            'bodyParam': 'bar'
        })

        self.transporter = Transporter(self.requester, self.config)

    def test_success_write(self):
        response = self.transporter.write('post', 'endpoint/foo', self.data,
                                          self.request_options)

        host = self.config.hosts['write']._hosts[0]  # type: Host

        self.requester.request.assert_called_once_with(
            'POST',  # Upper case letters
            'https://' + host.url + '/endpoint/foo?createIfNotExists=True',
            self.request_options.headers,
            self.data,
            5  # Default timeout
        )

        self.assertEqual({'foo': 'bar'}, response)
        self.assertEqual(self.requester.request.call_count, 1)

    def test_success_read(self):
        response = self.transporter.read('get', 'endpoint/bar',
                                         self.request_options)

        host = self.config.hosts['read']._hosts[0]  # type: Host

        self.requester.request.assert_called_once_with(
            'GET',  # Upper case letters
            'https://' + host.url + '/endpoint/bar?createIfNotExists=True',
            self.request_options.headers,
            {},
            109  # Customized timeout
        )

        self.assertEqual({'foo': 'bar'}, response)
        self.assertEqual(self.requester.request.call_count, 1)

    def test_unreachable_hosts_exception(self):
        self.requester.request.return_value = Response(300, {'foo': 'bar'})

        with self.assertRaises(AlgoliaUnreachableHostException) as _:
            self.transporter.read('get', 'endpoint/bar',
                                  self.request_options)

        self.assertEqual(self.requester.request.call_count, 5)

        self.requester.request.return_value = Response(100, {'foo': 'bar'})

        with self.assertRaises(AlgoliaUnreachableHostException) as _:
            self.transporter.read('get', 'endpoint/bar',
                                  self.request_options)
        self.assertEqual(self.requester.request.call_count, 10)  # 5 + 5

    def test_algolia_exception(self):
        self.requester.request.return_value = Response(401, {'foo': 'bar'})

        with self.assertRaises(AlgoliaException) as _:
            self.transporter.read('get', 'endpoint/bar',
                                  self.request_options)
        self.assertEqual(self.requester.request.call_count, 1)


class TestRetryStrategy(unittest.TestCase):
    def setUp(self):
        self.time = time.time()
        self.retry_strategy = RetryStrategy()
        self.host = Host('foo.com')

    def test_success_decision(self):
        decision = self.retry_strategy.decide(self.host, 200, False)

        self.assertEqual(decision, RetryOutcome.SUCCESS)
        self.assertEqual(self.host.up, True)
        self.assertGreaterEqual(self.host.last_use, self.time)
        self.assertEqual(self.host.retry_count, 0)

    def test_retryable_decision_because_status_code(self):
        decision = self.retry_strategy.decide(self.host, 300, False)

        self.assertEqual(decision, RetryOutcome.RETRY)
        self.assertEqual(self.host.up, False)
        self.assertGreaterEqual(self.host.last_use, self.time)
        self.assertEqual(self.host.retry_count, 0)

    def test_retryable_decision_because_timed_out(self):
        decision = self.retry_strategy.decide(self.host, 0, True)

        self.assertEqual(decision, RetryOutcome.RETRY)
        self.assertEqual(self.host.up, True)
        self.assertGreaterEqual(self.host.last_use, self.time)
        self.assertEqual(self.host.retry_count, 1)

    def test_fail_decision(self):
        decision = self.retry_strategy.decide(self.host, 401, False)

        self.assertEqual(decision, RetryOutcome.FAIL)
        self.assertEqual(self.host.up, True)
        self.assertGreaterEqual(self.host.last_use, self.time)
        self.assertEqual(self.host.retry_count, 0)
