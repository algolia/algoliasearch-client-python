# -*- coding: utf-8 -*-

from .user_insights_client import UserInsightsClient


class InsightsClient:
    def __init__(self, transport, region):
        self.__transport = transport
        self.__path = '/1/events'
        self.__transport.read_hosts = ['insights.' + region + '.algolia.io']
        self.__transport.write_hosts = ['insights.' + region + '.algolia.io']

    def user(self, user_token):
        return UserInsightsClient(self, user_token)

    def send_event(self, params, request_options=None):
        self.send_events([params], request_options)

    def send_events(self, events, request_options=None):
        self.post({'events': events}, request_options)

    def post(self, data, request_options=None):
        return self.__transport.req(False, self.__path, 'POST', {}, data, request_options)
