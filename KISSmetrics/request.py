# -*- coding: utf-8 -*-

RECORD_URI = '/e'
SET_URI = '/t'
ALIAS_URI = '/a'


from urllib import urlencode
from KISSmetrics import QueryString


def record(key, person, event, timestamp=None, properties={}):
    request = QueryString(key, person, event=event, timestamp=timestamp,
                          properties=properties)
    return '%s?%s' % (RECORD_URI, request.query_string)


def set(key, person, timestamp=None, properties={}):
    request = QueryString(key, person, timestamp=timestamp,
                          properties=properties)
    return '%s?%s' % (SET_URI, request.query_string)


def alias(key, person, identity):
    request = QueryString(key, person, identity=identity)
    return '%s?%s' % (ALIAS_URI, request.query_string)
