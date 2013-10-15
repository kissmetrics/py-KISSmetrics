# -*- coding: utf-8 -*-

from urllib3 import PoolManager

TRACKING_HOSTNAME = 'trk.kissmetrics.com'
TRACKING_PROTOCOL = 'http'

class Client:

    def __init__(self, key=None, trk_host=TRACKING_HOSTNAME,
                 trk_protocol=TRACKING_PROTOCOL):
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
