# -*- coding: utf-8 -*-


import KISSmetrics
from KISSmetrics import Client


class ClientCompat:

    def __init__(self, key, trk_host=KISSmetrics.TRACKING_HOSTNAME, trk_proto=KISSmetrics.TRACKING_PROTOCOL):
        self.client = Client(key=key, trk_host=trk_host, trk_proto=trk_proto)
        self.identity = None

    def identify(self, identity):
        self.identity = identity

    def url(self, query_string):
        return self.client.url(query_string)

    def record(self, event, properties={}, timestamp=None, uri=KISSmetrics.RECORD_URI):
        return self.client.record(person=self.identity, event=event, properties=properties, timestamp=timestamp, uri=uri)

    def set(self, properties={}, timestamp=None, uri=KISSmetrics.SET_URI):
        return self.client.set(person=self.identity, properties=properties, timestamp=timestamp, uri=uri)

    def alias(self, identity, uri=KISSmetrics.ALIAS_URI):
        return self.client.alias(person=self.identity, identity=identity, uri=uri)
