from collections import namedtuple


FakeResp = namedtuple('FakeResp', ['status_code', 'json'])


class FakeSession:
    def __init__(self, exp_headers, exp_params):
        self.headers = exp_headers
        self.params = exp_params

    def request(self, path, meth, timeout, params, data, headers):
        assert headers == self.headers
        assert params == self.params

        return FakeResp(status_code=200, json=lambda: '{}')
