import time
import unittest
import mock as mock

from algoliasearch.configs import SearchConfig
from algoliasearch.exceptions import (
    AlgoliaUnreachableHostException,
    AlgoliaException
)
from algoliasearch.http.hosts import Host, HostsCollection
from algoliasearch.http.request_options import RequestOptions
from algoliasearch.http.requester import Requester
from algoliasearch.http.transporter import (
    Transporter,
    Response,
    RetryStrategy,
    RetryOutcome,
    Request
)


class TestTransporter(unittest.TestCase):
    def setUp(self):
        self.requester = Requester()
        self.requester.send = mock.Mock(name="send")
        self.requester.send.return_value = Response(200, {'foo': 'bar'})

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

        host = self.config.hosts.write()[
            0]  # type: Host

        request = Request(
            'POST',
            self.request_options.headers,
            self.data,
            2,  # Default connect timeout
            30,  # Default timeout
        )

        request.url = 'https://{}/endpoint/foo?createIfNotExists=true'.format(
            host.url)

        self.requester.send.assert_called_once_with(request)

        self.assertEqual({'foo': 'bar'}, response)
        self.assertEqual(self.requester.send.call_count, 1)

    def test_success_read(self):
        response = self.transporter.read('get', 'endpoint/bar', {},
                                         self.request_options)

        host = self.config.hosts.read()[0]  # type: Host

        request = Request(
            'GET',  # Upper case letters
            self.request_options.headers,
            {'bodyParam': 'bar'},
            2,  # Default connect timeout
            109  # Customized timeout
        )
        request.url = 'https://{}/endpoint/bar?createIfNotExists=true'.format(
            host.url)

        self.requester.send.assert_called_once_with(request)

        self.assertEqual({'foo': 'bar'}, response)
        self.assertEqual(self.requester.send.call_count, 1)

    def test_unreachable_hosts_exception(self):
        self.requester.send.return_value = Response(300, {'foo': 'bar'})

        with self.assertRaises(AlgoliaUnreachableHostException) as _:
            self.transporter.read('get', 'endpoint/bar', {},
                                  self.request_options)

        self.assertEqual(self.requester.send.call_count, 4)

        self.requester.send.return_value = Response(100, {'foo': 'bar'})

        with self.assertRaises(AlgoliaUnreachableHostException) as _:
            self.transporter.read('get', 'endpoint/bar', {},
                                  self.request_options)
        # Remains 4, all hosts here down.
        self.assertEqual(self.requester.send.call_count, 4)

        with self.assertRaises(AlgoliaUnreachableHostException) as _:
            self.transporter.write('get', 'endpoint/bar', {},
                                   self.request_options)

        # It's now 5, write have one different host.
        self.assertEqual(self.requester.send.call_count, 5)

        with self.assertRaises(AlgoliaUnreachableHostException) as _:
            self.transporter.write('get', 'endpoint/bar', {},
                                   self.request_options)

        # Remains 5, all hosts here down.
        self.assertEqual(self.requester.send.call_count, 5)

    def test_algolia_exception(self):
        self.requester.send.return_value = Response(401, {'foo': 'bar'})

        with self.assertRaises(AlgoliaException) as _:
            self.transporter.read('get', 'endpoint/bar', {},
                                  self.request_options)
        self.assertEqual(self.requester.send.call_count, 1)


class TestRetryStrategy(unittest.TestCase):
    def setUp(self):
        self.time = time.time()
        self.retry_strategy = RetryStrategy()
        self.host = Host('foo.com')
        self.response = Response()

    def test_success_decision(self):
        self.response.status_code = 200
        decision = self.retry_strategy.decide(self.host, self.response)

        self.assertEqual(decision, RetryOutcome.SUCCESS)
        self.assertEqual(self.host.up, True)
        self.assertGreaterEqual(self.host.last_use, self.time)
        self.assertEqual(self.host.retry_count, 0)

    def test_retryable_decision_because_status_code(self):
        self.response.status_code = 300
        decision = self.retry_strategy.decide(self.host, self.response)

        self.assertEqual(decision, RetryOutcome.RETRY)
        self.assertEqual(self.host.up, False)
        self.assertGreaterEqual(self.host.last_use, self.time)
        self.assertEqual(self.host.retry_count, 0)

    def test_retryable_decision_because_timed_out(self):
        self.response.is_timed_out_error = True
        decision = self.retry_strategy.decide(self.host, self.response)

        self.assertEqual(decision, RetryOutcome.RETRY)
        self.assertEqual(self.host.up, True)
        self.assertGreaterEqual(self.host.last_use, self.time)
        self.assertEqual(self.host.retry_count, 1)

    def test_fail_decision(self):
        self.response.status_code = 401
        decision = self.retry_strategy.decide(self.host, self.response)

        self.assertEqual(decision, RetryOutcome.FAIL)
        self.assertEqual(self.host.up, True)
        self.assertGreaterEqual(self.host.last_use, self.time)
        self.assertEqual(self.host.retry_count, 0)

    def test_down_hosts(self):
        a = Host('a', 10)
        b = Host('b', 20)
        c = Host('c')

        self.retry_strategy._now = mock.Mock(
            name="_now")
        self.retry_strategy._now.return_value = 1000

        hosts = list(self.retry_strategy.valid_hosts([a, b, c]))
        self.assertEqual(len(hosts), 3)

        a.last_use = 800.0  # 1000 - 800 = 200 (lower than TTL - 300)
        a.up = False
        hosts = list(self.retry_strategy.valid_hosts([a, b, c]))
        self.assertEqual(len(hosts), 2)  # still down

        a.last_use = 400.0  # 1000 - 400 = 600 (bigger than TTL - 300)
        hosts = list(self.retry_strategy.valid_hosts([a, b, c]))
        self.assertEqual(len(hosts), 3)  # got up


class TestHostCollection(unittest.TestCase):

    def test_hosts_got_sorted(self):
        collection = HostsCollection([
            Host('a', 10),
            Host('b', 20),
            Host('c')
        ])

        hosts = collection.read()

        self.assertEqual(hosts[0].url, 'b')
        self.assertEqual(hosts[1].url, 'a')
        self.assertEqual(hosts[2].url, 'c')
