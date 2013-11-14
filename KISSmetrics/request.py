# -*- coding: utf-8 -*-

import KISSmetrics
from KISSmetrics.query_string import create_query

try:
    from urlparse import urlunsplit, SplitResult
except ImportError:
    from urllib.parse import urlunsplit, SplitResult


def _request(scheme=None, netloc=None, path=None, query=None, fragment=None):
    split = SplitResult(scheme=scheme, netloc=netloc, path=path, query=query,
                        fragment=None)
    return urlunsplit(split)


def record(key, person, event, timestamp=None, properties=None,
           scheme=KISSmetrics.TRACKING_SCHEME,
           host=KISSmetrics.TRACKING_HOSTNAME,
           path=KISSmetrics.RECORD_PATH):
    query = create_query(key, person, event=event, timestamp=timestamp,
                         properties=properties)
    return _request(scheme=scheme, netloc=host, path=path, query=query,
                    fragment=None)


def set(key, person, timestamp=None, properties=None,
        scheme=KISSmetrics.TRACKING_SCHEME,
        host=KISSmetrics.TRACKING_HOSTNAME,
        path=KISSmetrics.SET_PATH):
    query = create_query(key, person, timestamp=timestamp,
                         properties=properties)
    return _request(scheme=scheme, netloc=host, path=path, query=query,
                    fragment=None)


def alias(key, person, identity,
          scheme=KISSmetrics.TRACKING_SCHEME,
          host=KISSmetrics.TRACKING_HOSTNAME,
          path=KISSmetrics.ALIAS_PATH):
    query = create_query(key, person, identity=identity)
    return _request(scheme=scheme, netloc=host, path=path, query=query,
                    fragment=None)
