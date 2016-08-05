import os
import json

from requests import Session

from .helpers import urlify, CustomJSONEncoder, AlgoliaException

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

APPENGINE = 'APPENGINE_RUNTIME' in os.environ
SSL_CERTIFICATE_DOMAIN = 'algolia.net'

if APPENGINE:
    from google.appengine.api import urlfetch
    APPENGINE_METHODS = {
        'GET': urlfetch.GET,
        'POST': urlfetch.POST,
        'PUT': urlfetch.PUT,
        'DELETE': urlfetch.DELETE
    }


class Transport():
    def __init__(self):
        self.headers = {}
        self.read_hosts = []
        self.write_hosts = []
        self.timeout = (2, 30)
        self.search_timeout = (2, 5)

        self.session = Session()
        self.session.verify = os.path.join(os.path.dirname(__file__),
                                           'resources/ca-bundle.crt')

    def _app_req(self, host, path, meth, timeout, params, data):
        """
        Perform an HTTPS request with AppEngine's urlfetch. SSL certificate
        will not validate when the request is on a domain which is not a
        aloglia.net subdomain, a SNI is not available by default on GAE. Hence,
        we do set validate_certificate to False when calling those domains.
        """
        meth = APPENGINE_METHODS.get(meth)
        if isinstance(timeout, tuple):
            timeout = timeout[1]

        url = 'https://%s%s' % (host, path)
        if params is not None:
            url = '%s?%s' % (url, urlencode(params))

        res = urlfetch.fetch(
            url=url, method=meth, payload=data, headers=self.headers,
            deadline=timeout,
            validate_certificate=host.endswith(SSL_CERTIFICATE_DOMAIN))

        content = None if res.content is None else json.loads(res.content)
        if res.status_code // 100 == 2 and content is not None:
            return content
        elif res.status_code // 100 == 4:
            message = 'HTTP Code: %d' % res.status_code
            if content is not None and content.get('message') is not None:
                message = content['message']
            raise AlgoliaException(message)
        else:
            message = '% Server Error: %s' % (res.status_code, res.content)
            raise Exception(message, response=res)

    def _session_req(self, host, path, meth, timeout, params, data):
        """Perform an HTTPS request with request's Session."""
        url = 'https://%s%s' % (host, path)
        res = self.session.request(
            meth, url, params=params, data=data, timeout=timeout,
            headers=self.headers)

        if res.status_code // 100 == 2:
            j = res.json()
            if j is not None:
                return j

        if res.status_code // 100 == 4:
            message = 'HTTP Code: %d' % (res.status_code)
            try:
              j = res.json()
            except:
              j = { 'message': res.text}
            if j is not None and 'message' in j:
                message = j['message']
            raise AlgoliaException(message)

        res.raise_for_status()

    def req(self, is_search, path, meth, params=None, data=None):
        """Perform an HTTPS request with retry logic."""
        if params is not None:
            params = urlify(params)

        if data is not None:
            data = json.dumps(data, cls=CustomJSONEncoder)

        if is_search:
            hosts = self.read_hosts
            timeout = self.search_timeout
        else:
            hosts = self.write_hosts
            timeout = self.timeout

        exceptions = {}
        for i, host in enumerate(hosts):
            if i > 1:
                if isinstance(timeout, tuple):
                    timeout = (timeout[0] + 2, timeout[1] + 10)
                else:
                    timeout += 10

            try:
                r = self._app_req if APPENGINE else self._session_req
                return r(host, path, meth, timeout, params, data)
            except AlgoliaException as e:
                raise e
            except Exception as e:
                exceptions[host] = "%s: %s" % (e.__class__.__name__, str(e))

        raise AlgoliaException('Unreachable hosts: %s' % exceptions)
