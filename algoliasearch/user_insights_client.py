# -*- coding: utf-8 -*-

class UserInsightsClient:
    def __init__(self, insights_client, user_token):
        self.__insights_client = insights_client
        self.__user_token = user_token

    def clicked_object_ids(self, event_name, index_name, object_ids, request_options=None):
        self.__insights_client.send_event({
            'eventType': 'click',
            'eventName': event_name,
            'index': index_name,
            'userToken': self.__user_token,
            'objectIds': object_ids
        }, request_options)

    def clicked_object_ids_after_search(self, event_name, index_name, object_ids, positions, query_id,
                                        request_options=None):
        self.__insights_client.send_event({
            'eventType': 'click',
            'eventName': event_name,
            'index': index_name,
            'userToken': self.__user_token,
            'objectIds': object_ids,
            'positions': positions,
            'queryId': query_id
        }, request_options)

    def clicked_filters(self, event_name, index_name, filters, request_options=None):
        self.__insights_client.send_event({
            'eventType': 'click',
            'eventName': event_name,
            'index': index_name,
            'userToken': self.__user_token,
            'filters': filters
        }, request_options)

    def converted_object_ids(self, event_name, index_name, object_ids, request_options=None):
        self.__insights_client.send_event({
            'eventType': 'conversion',
            'eventName': event_name,
            'index': index_name,
            'userToken': self.__user_token,
            'objectIds': object_ids
        }, request_options)

    def converted_object_ids_after_search(self, event_name, index_name, object_ids, query_id,
                                          request_options=None):
        self.__insights_client.send_event({
            'eventType': 'conversion',
            'eventName': event_name,
            'index': index_name,
            'userToken': self.__user_token,
            'objectIds': object_ids,
            'queryId': query_id
        }, request_options)

    def converted_filters(self, event_name, index_name, filters, request_options=None):
        self.__insights_client.send_event({
            'eventType': 'conversion',
            'eventName': event_name,
            'index': index_name,
            'userToken': self.__user_token,
            'filters': filters
        }, request_options)

    def viewed_object_ids(self, event_name, index_name, object_ids, request_options=None):
        self.__insights_client.send_event({
            'eventType': 'view',
            'eventName': event_name,
            'index': index_name,
            'userToken': self.__user_token,
            'objectIds': object_ids
        }, request_options)

    def viewed_filters(self, event_name, index_name, filters, request_options=None):
        self.__insights_client.send_event({
            'eventType': 'view',
            'eventName': event_name,
            'index': index_name,
            'userToken': self.__user_token,
            'filters': filters
        }, request_options)
