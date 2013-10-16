# -*- coding: utf-8 -*-

import KISSmetrics
from KISSmetrics import request
from urllib3 import PoolManager


class Client:

    def __init__(self, key, trk_host=KISSmetrics.TRACKING_HOSTNAME,
                 trk_proto=KISSmetrics.TRACKING_PROTOCOL):
        self.key = key
        self.trk_host = trk_host
        if trk_proto not in ['http', 'https']:
            raise ValueError('trk_proto must be one of (http, https)')
        self.trk_proto = trk_proto
        self.http = PoolManager()

    def url(self, query_string):
        return '%s://%s/%s' % (self.trk_proto, self.trk_host, query_string)

    def record(self, person, event, properties={}, timestamp=None,
               uri=KISSmetrics.RECORD_URI):
        this_request = request.record(self.key, person, event,
                                      timestamp=timestamp,
                                      properties=properties, uri=uri)
        url = self.url(this_request)
        return self.http.request('GET', url)

    def set(self, person, properties={}, timestamp=None,
            uri=KISSmetrics.SET_URI):
        this_request = request.set(self.key, person, timestamp=timestamp,
                                   properties=properties, uri=uri)
        url = self.url(this_request)
        return self.http.request('GET', url)

    def alias(self, person, identity, uri=KISSmetrics.ALIAS_URI):
        this_request = request.alias(self.key, person, identity, uri=uri)
        url = self.url(this_request)
        return self.http.request('GET', url)
