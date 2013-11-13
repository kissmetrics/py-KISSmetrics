# -*- coding: utf-8 -*-

import KISSmetrics
from KISSmetrics.query_string import create_query


def record(key, person, event, timestamp=None, properties=None,
           path=KISSmetrics.RECORD_PATH):
    query = create_query(key, person, event=event, timestamp=timestamp,
                         properties=properties)
    return '%s?%s' % (path, query)


def set(key, person, timestamp=None, properties=None, path=KISSmetrics.SET_PATH):
    query = create_query(key, person, timestamp=timestamp,
                         properties=properties)
    return '%s?%s' % (path, query)


def alias(key, person, identity, path=KISSmetrics.ALIAS_PATH):
    query = create_query(key, person, identity=identity)
    return '%s?%s' % (path, query)
