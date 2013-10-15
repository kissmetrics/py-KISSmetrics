# -*- coding: utf-8 -*-

from urllib3 import PoolManager


class Client:

    def __init__(self, key=None, trk_host="trk.kissmetrics.com",
                 trk_protocol="https"):
        self.key = key
        self.trk_host = trk_host
        self.trk_protocol = trk_protocol
        self.http = PoolManager()

    def record(self, person, event, timestamp=None, properties={}):
        pass

    def set(self, person, timestamp=None, properties={}):
        pass

    def alias(self, person, identity):
        pass
