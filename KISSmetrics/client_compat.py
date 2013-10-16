# -*- coding: utf-8 -*-


import KISSmetrics
from KISSmetrics import Client

import datetime


port_map = {'80': 'http', '443': 'https'}


class ClientCompat:

    def __init__(self, key, host=None, http_timeout=None, logging=True):
        self.key = key
        if host:
            (trk_host, trk_port) = host.split(':')
            try:
                trk_proto = port_map[trk_port]
            except KeyError:
                raise ValueError('port in supplied host is not 80 or 443')
        else:
            trk_host = KISSmetrics.TRACKING_HOSTNAME
            trk_proto = 'http'
        self.client = Client(key=key, trk_host=trk_host, trk_proto=trk_proto)
        self.identity = None

    def identify(self, identity):
        self.identity = identity

    def record(self, action, props=None, uri=KISSmetrics.RECORD_URI,
               resp=False):
        self.check_id_key()
        timestamp = None
        if not props:
            props = {}
        response = self.client.record(person=self.identity, event=action,
                                      properties=props, timestamp=timestamp,
                                      uri=uri)
        if resp:
            return response

    def set(self, data, uri=KISSmetrics.SET_URI, resp=False):
        self.check_id_key()
        timestamp = None
        response = self.client.set(person=self.identity, properties=data,
                                   timestamp=timestamp, uri=uri)
        if resp:
            return response

    def alias(self, name, alias_to, uri=KISSmetrics.ALIAS_URI, resp=False):
        self.check_init()
        response = self.client.alias(person=name, identity=alias_to, uri=uri)
        if resp:
            return response

    def log_file(self):
        return '/tmp/kissmetrics_error.log'

    def reset(self):
        self.identity = None
        self.key = None

    def check_identify(self):
        if self.identity is None:
            raise Exception('Need to identify first (KM.identify <user>)')

    def check_init(self):
        if self.key is None:
            raise Exception('Need to initialize first (KM.init <your_key>)')

    def now(self):
        return datetime.datetime.utcnow()

    def check_id_key(self):
        self.check_init()
        self.check_identify()
