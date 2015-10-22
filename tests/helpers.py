# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
from random import randint

from faker import Factory
from algoliasearch.client import Client


class FakeData(object):
    def __init__(self):
        self._fake = Factory.create('zh_CN')
        self._fake.seed(4242)
        self._generated_id = []

    def fake_contact(self, n=1):
        data = []
        for i in range(n):
            data.append({
                'name': self._fake.name(),
                'email': self._fake.email(),
                'phone': self._fake.phone_number(),
                'city': self._fake.city(),
                'country': self._fake.country()
            })

        return data[0] if n == 1 else data

    def generate_id(self):
        while True:
            new_id = randint(0, 100000)
            if new_id not in self._generated_id:
                self._generated_id.append(new_id)
                return str(new_id)


def get_api_client():    
    if 'APPENGINE_RUNTIME' in os.environ:
        from google.appengine.api import apiproxy_stub_map 
        from google.appengine.api import urlfetch_stub
        apiproxy_stub_map.apiproxy = apiproxy_stub_map.APIProxyStubMap() 
        apiproxy_stub_map.apiproxy.RegisterStub('urlfetch',  urlfetch_stub.URLFetchServiceStub())
    return Client(os.environ['ALGOLIA_APPLICATION_ID'],
                  os.environ['ALGOLIA_API_KEY'])


def safe_index_name(name):
    if 'TRAVIS' not in os.environ:
        return name
    job = os.environ['TRAVIS_JOB_NUMBER']
    return '{0}_travis-{1}'.format(name, job)
