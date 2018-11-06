import os
import time
from random import randint

from algoliasearch import algoliasearch
from faker import Faker


def check_credentials():
    credentials = [
        'ALGOLIA_APPLICATION_ID',
        'ALGOLIA_API_KEY',
        'ALGOLIA_SEARCH_API_KEY',
        'ALGOLIA_APP_ID_MCM',
        'ALGOLIA_API_KEY_MCM'
    ]

    for credential in credentials:
        if credential not in os.environ:
            print('environment variable {} not defined'.format(credential))
            assert False


is_community = 'IS_COMMUNITY' in os.environ


def index_name():
    name = 'algolia-python{}'.format(randint(1, 100000))

    if 'TRAVIS' in os.environ:
        name = 'TRAVIS_PYTHON_{}_id-{}'.format(name, os.environ['TRAVIS_JOB_NUMBER'])

    return name


class Factory:
    def __init__(self):
        self._faker = Faker('zh_CN')
        self.last_id = 0

    def contacts(self, count=1):
        data = []
        for _ in range(count):
            data.append({
                'name': self._faker.name(),
                'email': self._faker.email(),
                'phone': self._faker.phone_number(),
                'city': self._faker.city(),
                'country': self._faker.country()
            })

        return data[0] if count == 1 else data

    def with_objectids(self, ids):
        if isinstance(ids, str) or isinstance(ids, int):
            contacts = self.contacts()
            contacts['objectID'] = ids
            return contacts

        contacts = self.contacts(len(ids))
        for objid, contact in zip(ids, contacts):
            contact['objectID'] = objid

        return contacts

    def objectids(self, n=1):
        ids = [str(i) for i in range(self.last_id, self.last_id + n)]
        self.last_id += n
        return ids


def create_client(
        app_id_env='ALGOLIA_APPLICATION_ID',
        api_key_env='ALGOLIA_API_KEY'
):
    if 'APPENGINE_RUNTIME' in os.environ:
        from google.appengine.api import apiproxy_stub_map
        from google.appengine.api import urlfetch_stub

        apiproxy_stub_map.apiproxy = apiproxy_stub_map.APIProxyStubMap()
        apiproxy_stub_map.apiproxy.RegisterStub(
            'urlfetch', urlfetch_stub.URLFetchServiceStub()
        )

    check_credentials()
    try:
        return algoliasearch.Client(
            os.environ[app_id_env],
            os.environ[api_key_env]
        )
    except:
        raise RuntimeError(
            "{} and {} environement variables must be set".format(
                app_id_env, api_key_env
            )
        )


def create_index(clt):
    name = index_name()
    task = clt.delete_index(name)
    idx = clt.init_index(name)
    idx.wait_task(task['taskID'])

    return idx


class IndexWithData:
    def __init__(self, clt, factory=None):
        if factory is None:
            factory = Factory()

        self.data = factory.contacts(5)
        self._index = create_index(clt)
        task = self._index.add_objects(self.data)
        self._index.wait_task(task['taskID'])
        self.ids = task['objectIDs']

    def __getattr__(self, name):
        return getattr(self._index, name)


def rule_stub(objid='my-rule'):
    return {
        'objectID': objid,
        'condition': {
            'pattern': 'some text',
            'anchoring': 'is'
        },
        'consequence': {
            'params': {
                'query': 'other text'
            }
        }
    }


def wait_key(index, key, block=None):
    for _ in range(60):
        try:
            if isinstance(index, algoliasearch.Index):
                k = index.get_api_key_acl(key)
            else:
                k = index.get_api_key(key)
            if block is None or block(k):
                return
        except:
            pass
        # Not found.
        time.sleep(1)


def wait_missing_key(index, key):
    for _ in range(60):
        try:
            if isinstance(index, algoliasearch.Index):
                index.get_api_key_acl(key)
            else:
                index.get_api_key(key)
            time.sleep(1)
        except:
            # Not found
            return
