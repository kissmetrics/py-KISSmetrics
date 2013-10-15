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

  def test_record_signature(self):
    with pytest.raises(TypeError):
      self.client.record()
    with pytest.raises(TypeError):
      self.client.record(person="foo@bar.baz")
    with pytest.raises(TypeError):
      self.client.record(event="fizz")


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

class KISSmetricsRequestFunctionsTestCase(unittest.TestCase):

  def test_record(self):
    query_string = KISSmetrics.request.record(key='foo', person='bar', event='fizzed')
    assert query_string == "_n=fizzed&_k=foo&_p=bar"

  def test_set(self):
    properties = {'cool': '1'}
    query_string = KISSmetrics.request.set(key='foo', person='bar', properties=properties)
    assert query_string == 'cool=1&_k=foo&_p=bar'

  def test_alias(self):
    query_string = KISSmetrics.request.alias(key='foo', person='bar', identity='baz')
    assert query_string == '_n=baz&_k=foo&_p=bar'

