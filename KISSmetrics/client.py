import KISSmetrics
from KISSmetrics import request
from urllib3 import PoolManager


class Client(object):

    def __init__(self, key, trk_host=KISSmetrics.TRACKING_HOSTNAME,
                 trk_proto=KISSmetrics.TRACKING_PROTOCOL):
        self.key = key
        if trk_proto not in ('http', 'https'):
            raise ValueError('trk_proto must be one of (http, https)')
        self.http = PoolManager()
        self.trk_host = trk_host
        self.trk_proto = trk_proto

    def request(self, query, method="GET"):
        url = '%s://%s/%s' % (self.trk_proto, self.trk_host, query)
        return self.http.request(method, url)

    def record(self, person, event, properties=None, timestamp=None,
               path=KISSmetrics.RECORD_PATH):
        this_request = request.record(self.key, person, event,
                                      timestamp=timestamp,
                                      properties=properties, path=path)
        return self.request(this_request)

    def set(self, person, properties=None, timestamp=None,
            path=KISSmetrics.SET_PATH):
        this_request = request.set(self.key, person, timestamp=timestamp,
                                   properties=properties, path=path)
        return self.request(this_request)

    def alias(self, person, identity, path=KISSmetrics.ALIAS_PATH):
        this_request = request.alias(self.key, person, identity, path=path)
        return self.request(this_request)
