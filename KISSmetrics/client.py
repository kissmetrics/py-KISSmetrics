# -*- coding: utf-8 -*-

import KISSmetrics
from KISSmetrics import request
from urllib3 import PoolManager


class Client:
    """Interface to KISSmetrics tracking service"""

    def __init__(self, key, trk_host=KISSmetrics.TRACKING_HOSTNAME,
                 trk_proto=KISSmetrics.TRACKING_PROTOCOL):
        """Initialize client for use with KISSmetrics API key.

        :param key: the API key is found on the "KISSmetrics Settings"
                    for a product.
        :type key: str

        :param trk_host: tracking URL for all requests; defaults
                         production tracking service.
        :param trk_proto: the protocol for requests; either be `'http'`
                          or `'https'`.

        """
        self.key = key
        if trk_proto not in ['http', 'https']:
            raise ValueError('trk_proto must be one of (http, https)')
        self.http = PoolManager()
        self.trk_host = trk_host
        self.trk_proto = trk_proto

    def request(self, query, method="GET"):
        url = '%s://%s/%s' % (self.trk_proto, self.trk_host, query)
        return self.http.request(method, url)

    def record(self, person, event, properties=None, timestamp=None,
               uri=KISSmetrics.RECORD_URI):
        """Record `event` for `person` with any `properties`.

        :param person: the individual performing the `event`
        :param event: the `event` name that was performed
        :param properties: any additional data to include
        :type properties: dict
        :param timestamp: when the `event` was performed; optional for
                          back-dating
        :param uri: HTTP endpoint to use; defaults to
                    ``KISSmetrics.RECORD_URI``

        :returns: an HTTP response for the request
        :rtype: `urllib3.response.HTTPResponse`

        """
        this_request = request.record(self.key, person, event,
                                      timestamp=timestamp,
                                      properties=properties, uri=uri)
        return self.request(this_request)

    def set(self, person, properties=None, timestamp=None,
            uri=KISSmetrics.SET_URI):
        """Set a property (or properties) for a `person`.

        :param person: the individual to associated properties with
        :param properties: key-value pairs to associated with `person`
        :type properties: dict
        :param timestamp: when the `event` was performed; optional for
                          back-dating
        :param uri: HTTP endpoint to use; defaults to
                    ``KISSmetrics.SET_URI``

        :returns: an HTTP response for the request
        :rtype: `urllib3.response.HTTPResponse`

        """
        this_request = request.set(self.key, person, timestamp=timestamp,
                                   properties=properties, uri=uri)
        return self.request(this_request)

    def alias(self, person, identity, uri=KISSmetrics.ALIAS_URI):
        """Map `person` to `identity`; actions done by one resolve the other.

        :param person: consider as same individual ``identity``; the
                       source of the alias operation
        :type person: str or unicode
        :param identity: consider as an alias of ``person``; the target
                         of the alias operation
        :type identity: str or unicode
        :param uri: HTTP endpoint to use; defaults to
                    ``KISSmetrics.ALIAS_URI``

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
        this_request = request.alias(self.key, person, identity, uri=uri)
        return self.request(this_request)
