# -*- coding: utf-8 -*-

import KISSmetrics
from KISSmetrics.query_string import create_query


def record(key, person, event, timestamp=None, properties=None,
           uri=KISSmetrics.RECORD_URI):
    query = create_query(key, person, event=event, timestamp=timestamp,
                         properties=properties)
    return '%s?%s' % (uri, query)


def set(key, person, timestamp=None, properties=None, uri=KISSmetrics.SET_URI):
    query = create_query(key, person, timestamp=timestamp,
                         properties=properties)
    return '%s?%s' % (uri, query)


def alias(key, person, identity, uri=KISSmetrics.ALIAS_URI):
    query = create_query(key, person, identity=identity)
    return '%s?%s' % (uri, query)
