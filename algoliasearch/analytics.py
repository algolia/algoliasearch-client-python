# -*- coding: utf-8 -*-
from algoliasearch.helpers import AlgoliaException
from .helpers import safe


class Analytics:

    def __init__(self, client, _transport):
        self.client = client
        self._transport = _transport
        self._transport.read_hosts = ['analytics.algolia.com']
        self._transport.write_hosts = ['analytics.algolia.com']

    def get_ab_tests(self, args=None):
        params = {'offest': 0, 'limit': 10}
        if args is not None:
            params.update(args)

        return self._req('/2/abtests', 'GET', params)

    def add_ab_test(self, ab_test):
        return self._req('/2/abtests', 'POST', None, ab_test)

    def get_ab_test(self, ab_test_id):
        if ab_test_id == '':
            raise AlgoliaException('ab_test_id cannot be empty')

        return self._req('/2/abtests/%s' % safe(ab_test_id), 'GET')

    def stop_ab_test(self, ab_test_id):
        if ab_test_id == '':
            raise AlgoliaException('ab_test_id cannot be empty')

        return self._req('/2/abtests/%s/stop' % safe(ab_test_id), 'POST')

    def delete_ab_test(self, ab_test_id):
        if ab_test_id == '':
            raise AlgoliaException('ab_test_id cannot be empty')

        return self._req('/2/abtests/%s' % safe(ab_test_id), 'DELETE')

    def wait_task(self, index_name, task_id, time_before_retry=100, request_options=None):
        return self.client.wait_task(index_name, task_id, time_before_retry, request_options)

    def _req(self, path, method, params=None, data=None):
        return self._transport.req(False, path, method, params, data)
