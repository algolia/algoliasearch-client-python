import copy
import json
import os
import time

from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util import Retry

from .helpers import AlgoliaException, CustomJSONEncoder, rotate, urlify

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

APPENGINE = 'APPENGINE_RUNTIME' in os.environ
SSL_CERTIFICATE_DOMAIN = 'algolia.net'
DNS_TIMER_DELAY = 5 * 60 # 5 minutes

if APPENGINE:
    from google.appengine.api import urlfetch
    APPENGINE_METHODS = {
        'GET': urlfetch.GET,
        'POST': urlfetch.POST,
        'PUT': urlfetch.PUT,
        'DELETE': urlfetch.DELETE
    }


# urllib ultimately uses `/etc/resolv.conf` on linux to get its DNS resolution
# timeout, this is the settings allowing to change it.
if 'RES_OPTIONS' not in os.environ:
    os.environ['RES_OPTIONS'] = 'timeout:2 attempts:1'


class Transport(object):
    def __init__(self):
        self.headers = {}
        self.read_hosts = []
        self.write_hosts = []
        self.timeout = (2, 30)
        self.search_timeout = (2, 5)
        self.dns_timer = time.time()

        self.session = Session()
        # Ask urllib not to make retries on its own.
        self.session.mount('https://', HTTPAdapter(max_retries=Retry(connect=0)))

    @property
    def read_hosts(self):
        return self._read_hosts

    @read_hosts.setter
    def read_hosts(self, value):
        self._read_hosts = value
        self._original_read_hosts = value

    @property
    def write_hosts(self):
        return self._write_hosts

    @write_hosts.setter
    def write_hosts(self, value):
        self._write_hosts = value
        self._original_write_hosts = value

    def _app_req(self, host, path, meth, timeout, params, data, headers):
        """
        Perform an HTTPS request with AppEngine's urlfetch. SSL certificate
        will not validate when the request is on a domain which is not a
        algolia.net subdomain, a SNI is not available by default on GAE. Hence,
        we do set validate_certificate to False when calling those domains.
        """
        meth = APPENGINE_METHODS.get(meth)
        if isinstance(timeout, tuple):
            timeout = timeout[1]

        url = 'https://%s%s' % (host, path)
        if params is not None:
            url = '%s?%s' % (url, urlencode(params))

        res = urlfetch.fetch(
            url=url, method=meth, payload=data, headers=headers,
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

    def _session_req(self, host, path, meth, timeout, params, data, headers):
        """Perform an HTTPS request with request's Session."""
        url = 'https://%s%s' % (host, path)
        res = self.session.request(
            meth, url, params=params, data=data, timeout=timeout,
            headers=headers)

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

    def _rotate_hosts(self, is_search):
        if is_search:
            self._read_hosts = rotate(self._read_hosts)
        else:
            self._write_hosts = rotate(self._write_hosts)

    def _get_hosts(self, is_search):
        secs_since_rotate = time.time() - self.dns_timer
        if is_search:
            if secs_since_rotate < DNS_TIMER_DELAY:
                return self.read_hosts
            else:
                return self._original_read_hosts
        else:
            if secs_since_rotate < DNS_TIMER_DELAY:
                return self.write_hosts
            else:
                return self._original_write_hosts

    def req(self, is_search, path, meth, params, data, request_options=None):
        """Perform an HTTPS request with retry logic."""

        # Merge params and request_options params.
        params = {} if params is None else params.copy()
        if request_options is not None and request_options.parameters is not None:
            params.update(request_options.parameters)

        params = urlify(params)

        # Merge headers and request_options headers.
        headers = {} if self.headers is None else self.headers.copy()
        if request_options is not None and request_options.headers is not None:
            headers.update(request_options.headers)

        if data is not None:
            data = json.dumps(data, cls=CustomJSONEncoder)

        hosts = self._get_hosts(is_search)
        timeout = self.search_timeout if is_search else self.timeout

        exceptions = {}
        for i, host in enumerate(hosts):
            if i > 1:
                if isinstance(timeout, tuple):
                    timeout = (timeout[0] + 2, timeout[1] + 10)
                else:
                    timeout += 10

            try:
                r = self._app_req if APPENGINE else self._session_req
                return r(host, path, meth, timeout, params, data, headers)
            except AlgoliaException as e:
                raise e
            except Exception as e:
                self._rotate_hosts(is_search)
                self.dns_timer = time.time()
                exceptions[host] = "%s: %s" % (e.__class__.__name__, str(e))

        raise AlgoliaException('Unreachable hosts: %s' % exceptions)
