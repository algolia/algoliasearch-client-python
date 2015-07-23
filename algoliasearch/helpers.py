# -*- coding: utf-8 -*-
'''
Copyright (c) 2013 Algolia
http://www.algolia.com/
Thanks to Arthur Lenoir <arthur (at) lenoir.me> for the initial version.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import json
import os
import sys
import decimal
import time
import datetime
import warnings

if sys.version < '3':
    from urllib import quote
    from urllib import urlencode
else:
    from urllib.parse import quote
    from urllib.parse import urlencode

import urllib3


# Detect the http_proxy env variable to activate the proxy
http_proxy = os.environ.get('http_proxy') or os.environ.get(
    'HTTP_PROXY') or os.environ.get('https_proxy') or os.environ.get(
        'HTTPS_PROXY')

# if proxy is set, use it for connecting to algolia host
if http_proxy is not None:
    POOL_MANAGER = urllib3.ProxyManager(
        http_proxy,
        cert_reqs='CERT_REQUIRED',
        ca_certs=os.path.join(os.path.split(__file__)[0],
                              "resources/ca-bundle.crt"))
else:
    POOL_MANAGER = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=os.path.join(os.path.split(__file__)[0],
                              "resources/ca-bundle.crt"))


def deprecated(func):
    '''
    This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emmitted
    when the function is used.
    '''

    def newFunc(*args, **kwargs):
        warnings.warn('Call to deprecated function %s.' % func.__name__,
                      category=DeprecationWarning)
        return func(*args, **kwargs)

    newFunc.__name__ = func.__name__
    newFunc.__doc__ = func.__doc__
    newFunc.__dict__.update(func.__dict__)
    return newFunc


class AlgoliaException(Exception):
    '''Exception launched by Algolia Client when an error occured.'''


def AlgoliaUtils_request(headers, hosts, method, request, timeout, body=None):
    '''Util function used to send request.'''
    exceptions = {}
    cnt = 0
    for host in hosts:
        cnt += 1
        try:
            obj = None
            if body:
                obj = json.dumps(body,
                                 cls=JSONEncoderWithDatetimeAndDefaultToString)
            conn = POOL_MANAGER.connection_from_host(host, scheme='https')
            if cnt == 3:
                timeout = urllib3.util.timeout.Timeout(
                    connect=timeout.connect_timeout + 2,
                    read=timeout.read_timeout + 10)
            answer = conn.urlopen(method, request,
                                  headers=headers,
                                  body=obj,
                                  timeout=timeout)
            content = json.loads(answer.data.decode('utf-8'))
            if int(answer.status / 100) == 4:
                raise AlgoliaException(content['message'])
            elif int(answer.status / 100) == 2:
                return content
        except AlgoliaException as e:
            raise e
        except Exception as e:
            exceptions[host] = str(e)
            pass
    raise AlgoliaException(('%s %s' % ('Unreachable host:', exceptions)))


class JSONEncoderWithDatetimeAndDefaultToString(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            try:
                return int(time.mktime(obj.timetuple()))
            except:
                return 0
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        try:
            return json.JSONEncoder.default(self, obj)
        except:
            return str(obj)
