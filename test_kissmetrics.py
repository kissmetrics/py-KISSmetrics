#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import unittest

import KISSmetrics


class KISSmetricsClientTestCase(unittest.TestCase):

  def setUp(self):
    self.client = KISSmetrics.Client(key='foo')

  def test_client_key(self):
    assert self.client.key == 'foo'

  def test_client_http_object(self):
    http = self.client.http
    assert http.request('GET', 'http://httpbin.org').status == 200


class KISSmetricsRequestTestCase(unittest.TestCase):

  def test_minimum(self):
    request = KISSmetrics.Request(key='foo', person='bar')
    assert request.query_string == "_k=foo&_p=bar"

  def test_event(self):
    request = KISSmetrics.Request(key='foo', person='bar', event='fizzed')
    assert request.query_string == "_n=fizzed&_k=foo&_p=bar"

  def test_set(self):
    properties = {'cool': '1'}
    request = KISSmetrics.Request(key='foo', person='bar', properties=properties)
    assert request.query_string == 'cool=1&_k=foo&_p=bar'

  def test_alias(self):
    request = KISSmetrics.Request(key='foo', person='bar', identity='baz')
    assert request.query_string == '_n=baz&_k=foo&_p=bar'

  def test_timestamp(self):
    request = KISSmetrics.Request(key='foo', person='bar', timestamp=1381849312)
    assert request.query_string == '_t=1381849312&_d=1&_k=foo&_p=bar'

class KISSmetricsRequestFunctionsTestCase(unittest.TestCase):

  def test_record(self):
    query_string = KISSmetrics.request.record(key='foo', person='bar', event='fizzed')
    assert query_string == "/e?_n=fizzed&_k=foo&_p=bar"

  def test_record_with_timestamp(self):
    query_string = KISSmetrics.request.record(key='foo', person='bar', event='fizzed', timestamp=1381849312)
    assert query_string == "/e?_t=1381849312&_d=1&_k=foo&_n=fizzed&_p=bar"

  def test_set(self):
    properties = {'cool': '1'}
    query_string = KISSmetrics.request.set(key='foo', person='bar', properties=properties)
    assert query_string == '/t?cool=1&_k=foo&_p=bar'

  def test_set_with_timestamp(self):
    properties = {'cool': '1'}
    query_string = KISSmetrics.request.set(key='foo', person='bar', properties=properties, timestamp=1381849312)
    assert query_string == '/t?_t=1381849312&cool=1&_d=1&_k=foo&_p=bar'

  def test_alias(self):
    query_string = KISSmetrics.request.alias(key='foo', person='bar', identity='baz')
    assert query_string == '/a?_n=baz&_k=foo&_p=bar'
