# -*- coding: utf-8 -*-

import KISSmetrics
from KISSmetrics import request
from urllib3 import PoolManager


class Client:
    """The client provides operations for reporting occurrences within back-end
    systems to KISSmetrics via either HTTP or HTTPS. It allows for recording
    events, setting properties, and aliasing identities.
    """
    def __init__(self, key, trk_host=KISSmetrics.TRACKING_HOSTNAME,
                 trk_proto=KISSmetrics.TRACKING_PROTOCOL):
        """Constructs instance given the API `key` for the KISSmetrics product.

        By default, the object will be constructed with `trk_host` set to the
        Production KISSmetrics tracking service via the `trk_proto`.

        ``key``       - the API key is found on the ``KISSmetrics Settings``
                        for a product.
        ``trk_host``  - the URL for all requests, it can be changes from the
                        default, production value for Tracking service.
        ``trk_proto`` - the protocol used for requests, it can be set but must
                        either be HTTP or HTTPS.
        """
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
