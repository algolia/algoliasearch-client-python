import sys
import os
import pytest

from .helpers.factory import Factory

is_community = 'IS_COMMUNITY' in os.environ

credentials = [
    'ALGOLIA_APPLICATION_ID_1',
    'ALGOLIA_ADMIN_KEY_1',
    'ALGOLIA_APPLICATION_ID_2',
    'ALGOLIA_ADMIN_KEY_2',
]

for credential in credentials:
    if credential not in os.environ:
        pytest.fail('Environment variable {} not defined'.format(credential))
        exit(1)

if is_community:

    credentials = [
        'ALGOLIA_APP_ID_MCM',
        'ALGOLIA_API_KEY_MCM',
    ]

    for credential in credentials:
        if credential not in os.environ:
            pytest.fail('Environment variable {} not defined'.format(credential))
            exit(1)

sys.path.append(os.path.join(os.path.dirname(__file__), 'helpers'))

@pytest.fixture
def client_1():
    app_id = os.environ['ALGOLIA_APPLICATION_ID_1']
    api_key = os.environ['ALGOLIA_ADMIN_KEY_1']
    return Factory.client(app_id, api_key)

@pytest.fixture
def client(client_1):
    return client_1;

@pytest.fixture
def index(client, request):
    index = Factory.index(client, request.node.name)

    yield index
    # index.delete()  # Tear down

@pytest.fixture
def obj():
    return Factory.obj()
