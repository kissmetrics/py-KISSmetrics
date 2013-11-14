# -*- coding: utf-8 -*-

import KISSmetrics
from KISSmetrics import Client

import datetime


port_map = {'80': 'http', '443': 'https'}


class ClientCompat(object):
    """Compatibility interface to KISSmetrics tracking service

    .. warning::

        Interface only exists for compatibility and will not be supported
        in the future.

    """

    def __init__(self, key, host=None, http_timeout=None, logging=True):
        """Initialize client for use with KISSmetrics API key.

        :param key: API key for a product, found on the
                    "KISSmetrics Settings".
        :type key: str
        :param host: tracking host for requests; defaults
                     production tracking service.
        :param http_timeout: request timeout; defaults to None
        :type http_timeout: int
        :param logging: indicate whether to log

        """
        self.key = key
        if host:
            (trk_host, trk_port) = host.split(':')
            try:
                trk_scheme = port_map[trk_port]
            except KeyError:
                raise ValueError('port in supplied host is not 80 or 443')
        else:
            trk_host = KISSmetrics.TRACKING_HOSTNAME
            trk_scheme = 'http'
        self.client = Client(key=key, trk_host=trk_host, trk_scheme=trk_scheme)
        self.identity = None

    def identify(self, identity):
        """Define identity for subsequent calls.

        :param identity: identifying info (email, user-id, anonymous-id)
        :type identity: str or unicode

        """
        self.identity = identity

    def record(self, action, props=None, path=KISSmetrics.RECORD_PATH,
               resp=False):
        """Record event for identity with any properties.

        :param action: event performed
        :param props: any additional data to include
        :type props: dict
        :param resp: indicate whether to return response
        :type resp: boolean

        :returns: an HTTP response for request if `resp=True`
        :rtype: `urllib3.response.HTTPResponse`

        :raises: Exception if either `identity` or `key` not set

        """
        self.check_id_key()
        timestamp = None
        if not props:
            props = {}
        response = self.client.record(person=self.identity, event=action,
                                      properties=props, timestamp=timestamp,
                                      path=path)
        if resp:
            return response

    def set(self, data, path=KISSmetrics.SET_PATH, resp=False):
        """Set a properties provided in `data` for identity.

        :param data: key-value pairs to associate with identity
        :type data: dict
        :param path: endpoint path; defaults to ``KISSmetrics.SET_PATH``
        :param resp: indicate whether to return response
        :type resp: boolean

        :returns: an HTTP response for request if `resp=True`
        :rtype: `urllib3.response.HTTPResponse`

        :raises: Exception if either `identity` or `key` not set

        """
        self.check_id_key()
        timestamp = None
        response = self.client.set(person=self.identity, properties=data,
                                   timestamp=timestamp, path=path)
        if resp:
            return response

    def alias(self, name, alias_to, path=KISSmetrics.ALIAS_PATH, resp=False):
        """Map `name` to `alias_to`; actions done by one resolve to other.

        :param name: consider as same individual as ``alias_to``
        :param alias_to: consider an alias of ``name``
        :param path: endpoint path; defaults to ``KISSmetrics.ALIAS_PATH``
        :param resp: indicate whether to return response
        :type resp: boolean

        :returns: an HTTP response for request if `resp=True`
        :rtype: `urllib3.response.HTTPResponse`

        :raises: Exception if either `identity` or `key` not set

        """
        self.check_init()
        response = self.client.alias(person=name, identity=alias_to, path=path)
        if resp:
            return response

    def log_file(self):
        """Retrieve path to log file.

        .. note::

            Will log to ``'/tmp/kissmetrics_error.log'``; cannot be modified.

        """
        return '/tmp/kissmetrics_error.log'

    def reset(self):
        """Reset `identity` and `key` attributes.

        .. warning::

            After calling this method, further calls to `record`, `set`, &
            `alias` will raise an `Exception`. You will need to set the API
            key again via `key` attribute and call `identify`.

        """
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
