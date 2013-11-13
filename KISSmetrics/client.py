# -*- coding: utf-8 -*-

import KISSmetrics
from KISSmetrics import request
from urllib3 import PoolManager


class Client:

    def __init__(self, key, trk_host=KISSmetrics.TRACKING_HOSTNAME,
                 trk_scheme=KISSmetrics.TRACKING_SCHEME):
        self.key = key
        if trk_scheme not in ['http', 'https']:
            raise ValueError('trk_scheme must be one of (http, https)')
        self.http = PoolManager()
        self.trk_host = trk_host
        self.trk_scheme = trk_scheme

    def request(self, uri, method="GET"):
        return self.http.request(method, uri)

    def record(self, person, event, properties=None, timestamp=None,
               path=KISSmetrics.RECORD_PATH):
        this_request = request.record(self.key, person, event,
                                      timestamp=timestamp,
                                      properties=properties,
                                      scheme=self.trk_scheme,
                                      host=self.trk_host, path=path)
        return self.request(this_request)

    def set(self, person, properties=None, timestamp=None,
            path=KISSmetrics.SET_PATH):
        this_request = request.set(self.key, person, timestamp=timestamp,
                                   properties=properties, scheme=self.trk_scheme,
                                   host=self.trk_host, path=path)
        return self.request(this_request)

    def alias(self, person, identity, path=KISSmetrics.ALIAS_PATH):
        this_request = request.alias(self.key, person, identity, scheme=self.trk_scheme,
                                     host=self.trk_host, path=path)
        return self.request(this_request)
