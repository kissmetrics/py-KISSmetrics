# -*- coding: utf-8 -*-

import KISSmetrics
from KISSmetrics.query_string import create_query

try:
    from urlparse import urlunsplit, SplitResult
except ImportError:
    from urllib.parse import urlunsplit, SplitResult


def record(key, person, event, timestamp=None, properties=None,
           scheme=KISSmetrics.TRACKING_SCHEME,
           host=KISSmetrics.TRACKING_HOSTNAME,
           path=KISSmetrics.RECORD_PATH):
    query = create_query(key, person, event=event, timestamp=timestamp,
                         properties=properties)
    split = SplitResult(scheme=scheme, netloc=host, path=path, query=query,
                        fragment=None)
    return urlunsplit(split)


def set(key, person, timestamp=None, properties=None,
        scheme=KISSmetrics.TRACKING_SCHEME,
        host=KISSmetrics.TRACKING_HOSTNAME,
        path=KISSmetrics.SET_PATH):
    query = create_query(key, person, timestamp=timestamp,
                         properties=properties)
    split = SplitResult(scheme=scheme, netloc=host, path=path, query=query,
                        fragment=None)
    return urlunsplit(split)


def alias(key, person, identity,
          scheme=KISSmetrics.TRACKING_SCHEME,
          host=KISSmetrics.TRACKING_HOSTNAME,
          path=KISSmetrics.ALIAS_PATH):
    query = create_query(key, person, identity=identity)
    split = SplitResult(scheme=scheme, netloc=host, path=path, query=query,
                        fragment=None)
    return urlunsplit(split)
