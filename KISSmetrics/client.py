# -*- coding: utf-8 -*-

import KISSmetrics
from KISSmetrics import request
from urllib3 import PoolManager


class Client:
    """provides operations for reporting occurrences within back-end
    systems to KISSmetrics via either HTTP or HTTPS. It allows for
    recording events, setting properties, and aliasing identities.

    """
    def __init__(self, key, trk_host=KISSmetrics.TRACKING_HOSTNAME,
                 trk_proto=KISSmetrics.TRACKING_PROTOCOL):
        """Constructs instance given the API `key` for the KISSmetrics
        product.

        :param key: the API key is found on the "KISSmetrics Settings"
                    for a product.
        :type key: str

        :param trk_host: tracking URL for all requests; defaults
                         production tracking service.
        :param trk_proto: the protocol for requests; either be HTTP or
                          HTTPS.

        """
        self.key = key
        self.trk_host = trk_host
        if trk_proto not in ['http', 'https']:
            raise ValueError('trk_proto must be one of (http, https)')
        self.trk_proto = trk_proto
        self.http = PoolManager()

    def url(self, query_string):
        """Handles formating the URL requests.

        :param query_string: the key-value pairs to include
        :type query_string: dict

        :returns: a formatted, valid URL given the protocol, host &
                  query string
        :rtype: str

        """
        return '%s://%s/%s' % (self.trk_proto, self.trk_host, query_string)

    def record(self, person, event, properties={}, timestamp=None,
               uri=KISSmetrics.RECORD_URI):
        """Records `event` for `person` with any `properties`.

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
        url = self.url(this_request)
        return self.http.request('GET', url)

    def set(self, person, properties={}, timestamp=None,
            uri=KISSmetrics.SET_URI):
        """Sets a property (or properties) for a `person`.

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
        url = self.url(this_request)
        return self.http.request('GET', url)

    def alias(self, person, identity, uri=KISSmetrics.ALIAS_URI):
        """Creates a mapping from ``person`` to ``identity`` such actions
        done by either are resolved to the same person.

        Note the direction of the mapping is ``person`` to ``identity``
        (so ``person`` is also known as ``identity`` or ``person`` =>
        ``identity`` when looking at it as "source => target")

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

        Aliasing is not a reversible operation.  When aliasing to an
        identity, take care not to use a session identifier or any other
        value that is not relatively stable (a value that will not
        change per request or per session).

        When consulting the Aliasing documentation, `person` corresponds
        to ``query_string.PERSON_PARAM`` and `identity` corresponds to
        ``query_string.ALIAS_PARAM``.

        For more information see the API Specifications on `Aliasing
        <http://support.kissmetrics.com/apis/specifications.html#aliasing-users>`_.

        """
        this_request = request.alias(self.key, person, identity, uri=uri)
        url = self.url(this_request)
        return self.http.request('GET', url)
