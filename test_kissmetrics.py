#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import unittest
import json

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

  def test_client_url(self):
    url = self.client.url('e?_k=foo&_p=bar')
    assert url == "http://trk.kissmetrics.com/e?_k=foo&_p=bar"

  def test_client_protocol(self):
    with pytest.raises(ValueError):
      client = KISSmetrics.Client(key='foo', trk_proto='ssh')

class KISSmetricsClientIntegrationCase(unittest.TestCase):

  def setUp(self):
    self.client = KISSmetrics.Client(key='foo', trk_host='httpbin.org')

  def test_record_success(self):
    response = self.client.record(person='bob', event='fizzed', uri='get')
    assert response.status == 200

  def test_record_key(self):
    response = self.client.record(person='bob', event='fizzed', uri='get')
    data = json.loads(response.data.decode())
    assert data['args']['_k'] == 'foo'

  def test_record_person(self):
    response = self.client.record(person='bob', event='fizzed', uri='get')
    data = json.loads(response.data.decode())
    assert data['args']['_p'] == 'bob'

  def test_record_event(self):
    response = self.client.record(person='bob', event='fizzed', uri='get')
    data = json.loads(response.data.decode())
    assert data['args']['_n'] == 'fizzed'

  def test_set_success(self):
    response = self.client.set(person='bob', properties={'cool': 1}, uri='get')
    assert response.status == 200

  def test_set_key(self):
    response = self.client.set(person='bob', properties={'cool': 1}, uri='get')
    data = json.loads(response.data.decode())
    assert data['args']['_k'] == 'foo'

  def test_set_person(self):
    response = self.client.set(person='bob', properties={'cool': 1}, uri='get')
    data = json.loads(response.data.decode())
    assert data['args']['_p'] == 'bob'

  def test_set_property(self):
    response = self.client.set(person='bob', properties={'cool': 1}, uri='get')
    data = json.loads(response.data.decode())
    assert data['args']['cool'] == '1'

  def test_alias_success(self):
    response = self.client.alias(person='bob', identity='shadybob', uri='get')
    assert response.status == 200

  def test_alias_person(self):
    response = self.client.alias(person='bob', identity='shadybob', uri='get')
    data = json.loads(response.data.decode())
    assert data['args']['_p'] == 'bob'

  def test_alias_identity(self):
    response = self.client.alias(person='bob', identity='shadybob', uri='get')
    data = json.loads(response.data.decode())
    assert data['args']['_n'] == 'shadybob'

class KISSmetricsRequestTestCase(unittest.TestCase):

  def test_minimum(self):
    request = KISSmetrics.QueryString(key='foo', person='bar')
    assert parse_qs(request.query_string)['_k'] == ['foo']
    assert parse_qs(request.query_string)['_p'] == ['bar']

  def test_event(self):
    request = KISSmetrics.QueryString(key='foo', person='bar', event='fizzed')
    assert parse_qs(request.query_string)['_k'] == ['foo']
    assert parse_qs(request.query_string)['_p'] == ['bar']
    assert parse_qs(request.query_string)['_n'] == ['fizzed']

  def test_set(self):
    properties = {'cool': '1'}
    request = KISSmetrics.QueryString(key='foo', person='bar', properties=properties)
    assert parse_qs(request.query_string)['_k'] == ['foo']
    assert parse_qs(request.query_string)['_p'] == ['bar']
    assert parse_qs(request.query_string)['cool'] == ['1']

  def test_alias(self):
    request = KISSmetrics.QueryString(key='foo', person='bar', identity='baz')
    assert parse_qs(request.query_string)['_k'] == ['foo']
    assert parse_qs(request.query_string)['_p'] == ['bar']
    assert parse_qs(request.query_string)['_n'] == ['baz']

  def test_timestamp(self):
    request = KISSmetrics.QueryString(key='foo', person='bar', timestamp=1381849312)
    assert parse_qs(request.query_string)['_k'] == ['foo']
    assert parse_qs(request.query_string)['_p'] == ['bar']
    assert parse_qs(request.query_string)['_d'] == ['1']
    assert parse_qs(request.query_string)['_t'] == ['1381849312']

class KISSmetricsRequestFunctionsTestCase(unittest.TestCase):

  def test_record(self):
    query_string = KISSmetrics.request.record(key='foo', person='bar', event='fizzed')
    assert urlparse(query_string).path == 'e'
    query_string = urlparse(query_string).query
    assert parse_qs(query_string)['_k'] == ['foo']
    assert parse_qs(query_string)['_p'] == ['bar']
    assert parse_qs(query_string)['_n'] == ['fizzed']

  def test_record_with_timestamp(self):
    query_string = KISSmetrics.request.record(key='foo', person='bar', event='fizzed', timestamp=1381849312)
    assert urlparse(query_string).path == 'e'
    query_string = urlparse(query_string).query
    assert parse_qs(query_string)['_k'] == ['foo']
    assert parse_qs(query_string)['_p'] == ['bar']
    assert parse_qs(query_string)['_d'] == ['1']
    assert parse_qs(query_string)['_t'] == ['1381849312']

  def test_record_custom_uri(self):
    query_string = KISSmetrics.request.record(key='foo', person='bar', event='fizzed', uri='get')
    assert urlparse(query_string).path == 'get'
    query_string = urlparse(query_string).query
    assert parse_qs(query_string)['_k'] == ['foo']
    assert parse_qs(query_string)['_p'] == ['bar']
    assert parse_qs(query_string)['_n'] == ['fizzed']

  def test_set(self):
    properties = {'cool': '1'}
    query_string = KISSmetrics.request.set(key='foo', person='bar', properties=properties)
    assert urlparse(query_string).path == 's'
    query_string = urlparse(query_string).query
    assert parse_qs(query_string)['_k'] == ['foo']
    assert parse_qs(query_string)['_p'] == ['bar']
    assert parse_qs(query_string)['cool'] == ['1']

  def test_set_with_timestamp(self):
    properties = {'cool': '1'}
    query_string = KISSmetrics.request.set(key='foo', person='bar', properties=properties, timestamp=1381849312)
    assert urlparse(query_string).path == 's'
    query_string = urlparse(query_string).query
    assert parse_qs(query_string)['_k'] == ['foo']
    assert parse_qs(query_string)['_p'] == ['bar']
    assert parse_qs(query_string)['_d'] == ['1']
    assert parse_qs(query_string)['_t'] == ['1381849312']
    assert parse_qs(query_string)['cool'] == ['1']

  def test_set_custom_uri(self):
    properties = {'cool': '1'}
    query_string = KISSmetrics.request.set(key='foo', person='bar', properties=properties, uri='get')
    assert urlparse(query_string).path == 'get'
    query_string = urlparse(query_string).query
    assert parse_qs(query_string)['_k'] == ['foo']
    assert parse_qs(query_string)['_p'] == ['bar']
    assert parse_qs(query_string)['cool'] == ['1']

  def test_alias(self):
    query_string = KISSmetrics.request.alias(key='foo', person='bar', identity='baz')
    assert urlparse(query_string).path == 'a'
    query_string = urlparse(query_string).query
    assert parse_qs(query_string)['_k'] == ['foo']
    assert parse_qs(query_string)['_p'] == ['bar']
    assert parse_qs(query_string)['_n'] == ['baz']

  def test_alias_custom_uri(self):
    query_string = KISSmetrics.request.alias(key='foo', person='bar', identity='baz', uri='get')
    assert urlparse(query_string).path == 'get'
    query_string = urlparse(query_string).query
    assert parse_qs(query_string)['_k'] == ['foo']
    assert parse_qs(query_string)['_p'] == ['bar']
    assert parse_qs(query_string)['_n'] == ['baz']
