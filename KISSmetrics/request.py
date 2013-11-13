# -*- coding: utf-8 -*-

import KISSmetrics
from KISSmetrics.query_string import create_query

def _request(scheme, host, path, query):
    return '%s://%s/%s?%s' % (scheme, host, path, query)

def record(key, person, event, timestamp=None, properties=None,
           scheme=KISSmetrics.TRACKING_SCHEME,
           host=KISSmetrics.TRACKING_HOSTNAME,
           path=KISSmetrics.RECORD_PATH):
    query = create_query(key, person, event=event, timestamp=timestamp,
                         properties=properties)
    return _request(scheme, host, path, query)


def set(key, person, timestamp=None, properties=None,
        scheme=KISSmetrics.TRACKING_SCHEME,
        host=KISSmetrics.TRACKING_HOSTNAME,
        path=KISSmetrics.SET_PATH):
    query = create_query(key, person, timestamp=timestamp,
                         properties=properties)
    return _request(scheme, host, path, query)


def alias(key, person, identity,
          scheme=KISSmetrics.TRACKING_SCHEME,
          host=KISSmetrics.TRACKING_HOSTNAME,
          path=KISSmetrics.ALIAS_PATH):
    query = create_query(key, person, identity=identity)
    return _request(scheme, host, path, query)
