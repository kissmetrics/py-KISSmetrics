# -*- coding: utf-8 -*-

import KISSmetrics


def record(key, person, event, timestamp=None, properties={},
           uri=KISSmetrics.RECORD_URI):
    request = KISSmetrics.QueryString(key, person, event=event, timestamp=timestamp,
                                      properties=properties)
    return '%s?%s' % (uri, request.query_string)


def set(key, person, timestamp=None, properties={}, uri=KISSmetrics.SET_URI):
    request = KISSmetrics.QueryString(key, person, timestamp=timestamp,
                                      properties=properties)
    return '%s?%s' % (uri, request.query_string)


def alias(key, person, identity, uri=KISSmetrics.ALIAS_URI):
    request = KISSmetrics.QueryString(key, person, identity=identity)
    return '%s?%s' % (uri, request.query_string)
