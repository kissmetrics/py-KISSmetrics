# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/..'))

import unittest
import pytest
import datetime

try:
    from urlparse import parse_qs
except:
    from urllib.parse import parse_qs

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

import KISSmetrics


class KISSmetricsClientTestCase(unittest.TestCase):

    def setUp(self):
        self.client = KISSmetrics.Client(key='foo')

    def test_client_key(self):
        assert self.client.key == 'foo'

    def test_client_http_object(self):
        http = self.client.http
        assert http.request('GET', 'http://httpbin.org').status == 200

    def test_client_scheme(self):
        with pytest.raises(ValueError):
            client = KISSmetrics.Client(key='foo', trk_scheme='ssh')
            del client


class KISSmetricsClientCompatTestCase(unittest.TestCase):

    def setUp(self):
        self.client = KISSmetrics.ClientCompat(key='foo')

    def test_compatibility_alias(self):
        self.client = KISSmetrics.KM('foo')
        assert self.client.client.key == 'foo'

    def test_client_compat_key(self):
        assert self.client.client.key == 'foo'

    def test_client_compat_http_object(self):
        http = self.client.client.http
        assert http.request('GET', 'http://httpbin.org').status == 200

    def test_client_compat_scheme(self):
        with pytest.raises(ValueError):
            client = KISSmetrics.ClientCompat(key='foo', host='trk.kissmetrics.com:22')
            del client

    def test_client_compat_log_file(self):
        assert self.client.log_file() == '/tmp/kissmetrics_error.log'

    def test_client_compat_check_identify(self):
        with pytest.raises(Exception):
            client = KISSmetrics.ClientCompat(key='foo')
            client.reset()
            client.check_identify()

    def test_client_compat_check_init(self):
        with pytest.raises(Exception):
            client = KISSmetrics.ClientCompat(key='foo')
            client.reset()
            client.check_init()

    def test_client_compat_now(self):
        now = datetime.datetime.now()
        assert now - self.client.now() < datetime.timedelta(seconds=5)


class KISSmetricsRequestTestCase(unittest.TestCase):

    def test_minimum(self):
        query = KISSmetrics.query_string.create_query(key='foo', person='bar')
        assert parse_qs(query)['_k'] == ['foo']
        assert parse_qs(query)['_p'] == ['bar']

    def test_event(self):
        query = KISSmetrics.query_string.create_query(key='foo', person='bar', event='fizzed')
        assert parse_qs(query)['_k'] == ['foo']
        assert parse_qs(query)['_p'] == ['bar']
        assert parse_qs(query)['_n'] == ['fizzed']

    def test_set(self):
        properties = {'cool': '1'}
        query = KISSmetrics.query_string.create_query(key='foo', person='bar', properties=properties)
        assert parse_qs(query)['_k'] == ['foo']
        assert parse_qs(query)['_p'] == ['bar']
        assert parse_qs(query)['cool'] == ['1']

    def test_alias(self):
        query = KISSmetrics.query_string.create_query(key='foo', person='bar', identity='baz')
        assert parse_qs(query)['_k'] == ['foo']
        assert parse_qs(query)['_p'] == ['bar']
        assert parse_qs(query)['_n'] == ['baz']

    def test_timestamp(self):
        query = KISSmetrics.query_string.create_query(key='foo', person='bar', timestamp=1381849312)
        assert parse_qs(query)['_k'] == ['foo']
        assert parse_qs(query)['_p'] == ['bar']
        assert parse_qs(query)['_d'] == ['1']
        assert parse_qs(query)['_t'] == ['1381849312']


class TestKISSmetricsRequestFunctionsTestCase(unittest.TestCase):

    def test_record(self):
        query_string = KISSmetrics.request.record(key='foo', person='bar', event='fizzed')
        assert urlparse(query_string).path == '/e'
        query_string = urlparse(query_string).query
        assert parse_qs(query_string)['_k'] == ['foo']
        assert parse_qs(query_string)['_p'] == ['bar']
        assert parse_qs(query_string)['_n'] == ['fizzed']

    def test_record_with_timestamp(self):
        query_string = KISSmetrics.request.record(key='foo', person='bar', event='fizzed', timestamp=1381849312)
        assert urlparse(query_string).path == '/e'
        query_string = urlparse(query_string).query
        assert parse_qs(query_string)['_k'] == ['foo']
        assert parse_qs(query_string)['_p'] == ['bar']
        assert parse_qs(query_string)['_d'] == ['1']
        assert parse_qs(query_string)['_t'] == ['1381849312']

    def test_record_custom_path(self):
        query_string = KISSmetrics.request.record(key='foo', person='bar', event='fizzed', path='get')
        assert urlparse(query_string).path == '/get'
        query_string = urlparse(query_string).query
        assert parse_qs(query_string)['_k'] == ['foo']
        assert parse_qs(query_string)['_p'] == ['bar']
        assert parse_qs(query_string)['_n'] == ['fizzed']

    def test_set(self):
        properties = {'cool': '1'}
        query_string = KISSmetrics.request.set(key='foo', person='bar', properties=properties)
        assert urlparse(query_string).path == '/s'
        query_string = urlparse(query_string).query
        assert parse_qs(query_string)['_k'] == ['foo']
        assert parse_qs(query_string)['_p'] == ['bar']
        assert parse_qs(query_string)['cool'] == ['1']

    def test_set_with_timestamp(self):
        properties = {'cool': '1'}
        query_string = KISSmetrics.request.set(key='foo', person='bar', properties=properties, timestamp=1381849312)
        assert urlparse(query_string).path == '/s'
        query_string = urlparse(query_string).query
        assert parse_qs(query_string)['_k'] == ['foo']
        assert parse_qs(query_string)['_p'] == ['bar']
        assert parse_qs(query_string)['_d'] == ['1']
        assert parse_qs(query_string)['_t'] == ['1381849312']
        assert parse_qs(query_string)['cool'] == ['1']

    def test_set_custom_path(self):
        properties = {'cool': '1'}
        query_string = KISSmetrics.request.set(key='foo', person='bar', properties=properties, path='get')
        assert urlparse(query_string).path == '/get'
        query_string = urlparse(query_string).query
        assert parse_qs(query_string)['_k'] == ['foo']
        assert parse_qs(query_string)['_p'] == ['bar']
        assert parse_qs(query_string)['cool'] == ['1']

    def test_alias(self):
        query_string = KISSmetrics.request.alias(key='foo', person='bar', identity='baz')
        assert urlparse(query_string).path == '/a'
        query_string = urlparse(query_string).query
        assert parse_qs(query_string)['_k'] == ['foo']
        assert parse_qs(query_string)['_p'] == ['bar']
        assert parse_qs(query_string)['_n'] == ['baz']

    def test_alias_custom_path(self):
        query_string = KISSmetrics.request.alias(key='foo', person='bar', identity='baz', path='get')
        assert urlparse(query_string).path == '/get'
        query_string = urlparse(query_string).query
        assert parse_qs(query_string)['_k'] == ['foo']
        assert parse_qs(query_string)['_p'] == ['bar']
        assert parse_qs(query_string)['_n'] == ['baz']


if __name__ == '__main__':
    unittest.main()
