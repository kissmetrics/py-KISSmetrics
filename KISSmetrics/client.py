# -*- coding: utf-8 -*-

import KISSmetrics
from KISSmetrics import request
from urllib3 import PoolManager


class Client(object):
    """Interface to KISSmetrics tracking service"""

    def __init__(self, key, trk_host=KISSmetrics.TRACKING_HOSTNAME,
                 trk_scheme=KISSmetrics.TRACKING_SCHEME):
        """Initialize client for use with KISSmetrics API key.

        :param key: API key for product, found on the
                    "KISSmetrics Settings".
        :type key: str
        :param trk_host: tracking host for requests; defaults
                         production tracking service.
        :param trk_proto: the protocol for requests; either be `'http'`
                          or `'https'`.

        """
        self.key = key
        if trk_scheme not in ('http', 'https'):
            raise ValueError('trk_scheme must be one of (http, https)')
        self.http = PoolManager()
        self.trk_host = trk_host
        self.trk_scheme = trk_scheme

    def record(self, person, event, properties=None, timestamp=None,
               path=KISSmetrics.RECORD_PATH):
        """Record `event` for `person` with any `properties`.

        :param person: the individual performing the `event`
        :param event: the `event` name that was performed
        :param properties: any additional data to include
        :type properties: dict
        :param timestamp: when the `event` was performed; optional for
                          back-dating
        :param path: HTTP endpoint to use; defaults to
                    ``KISSmetrics.RECORD_PATH``

        :returns: an HTTP response for the request
        :rtype: `urllib3.response.HTTPResponse`

        """
        this_request = request.record(self.key, person, event,
                                      timestamp=timestamp,
                                      properties=properties,
                                      scheme=self.trk_scheme,
                                      host=self.trk_host, path=path)
        return self._request(this_request)

    def set(self, person, properties=None, timestamp=None,
            path=KISSmetrics.SET_PATH):
        """Set a property (or properties) for a `person`.

        :param person: individual to associate properties with
        :param properties: key-value pairs to associate with `person`
        :type properties: dict
        :param timestamp: when the `event` was performed; optional for
                          back-dating
        :param path: HTTP endpoint to use; defaults to
                    ``KISSmetrics.SET_PATH``

        :returns: an HTTP response for the request
        :rtype: `urllib3.response.HTTPResponse`

        """
        this_request = request.set(self.key, person, timestamp=timestamp,
                                   properties=properties,
                                   scheme=self.trk_scheme, host=self.trk_host,
                                   path=path)
        return self._request(this_request)

    def alias(self, person, identity, path=KISSmetrics.ALIAS_PATH):
        """Map `person` to `identity`; actions done by one resolve to other.

        :param person: consider as same individual ``identity``; the
                       source of the alias operation
        :type person: str or unicode
        :param identity: consider as an alias of ``person``; the target
                         of the alias operation
        :type identity: str or unicode
        :param path: HTTP endpoint to use; defaults to
                    ``KISSmetrics.ALIAS_PATH``

        :returns: an HTTP response for the request
        :rtype: `urllib3.response.HTTPResponse`

        Note the direction of the mapping is ``person`` to ``identity``
        (so "``person`` is also known as ``identity``" or "``person`` =>
        ``identity``" when looking at it as "``<source>`` => ``<target>``")

        When consulting the Aliasing documentation, `person` corresponds
        to ``query_string.PERSON_PARAM`` and `identity` corresponds to
        ``query_string.ALIAS_PARAM``.

        Aliasing is not a reversible operation.  When aliasing to an
        identity, take care not to use a session identifier or any other
        value that is not relatively stable (a value that will not
        change per request or per session).

        For more information see the API Specifications on `Aliasing
        <http://support.kissmetrics.com/apis/specifications.html#aliasing-users>`_.

        """
        this_request = request.alias(self.key, person, identity,
                                     scheme=self.trk_scheme,
                                     host=self.trk_host, path=path)
        return self._request(this_request)

    def _request(self, uri, method='GET'):
        return self.http.request(method, uri)
