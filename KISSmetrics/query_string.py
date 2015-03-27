# -*- coding: utf-8 -*-

KEY_KEY = '_k'
PERSON_KEY = '_p'
EVENT_NAME_KEY = '_n'
TIME_KEY = '_t'
TIME_FLAG_KEY = '_d'
ALIAS_KEY = '_n'


try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


def create_query(key, person, event=None, timestamp=None,
                 identity=None, properties=None):
    """Build and encode query string.

    :param key: API key for product, found on the
                "KISSmetrics Settings".
    :param person: individual performing `event`
    :param event: event name that was performed
    :param timestamp: when `event` was performed; optional for
                      back-dating
    :param identity: individual to alias to `person`
    :param properties: any additional data to include
    :type properties: dict

    :returns: URL encoded string representing query string
    :rtype: str

    .. note::

        When a ``timestamp`` is provided, the ``TIME_FLAG_KEY`` will
        be set to ``1`` and included.

    """
    if properties is None:
        properties = {}

    query_dict = {KEY_KEY: key, PERSON_KEY: person}
    if timestamp:
        query_dict[TIME_FLAG_KEY] = 1
        query_dict[TIME_KEY] = int(timestamp)
    if event:
        query_dict[EVENT_NAME_KEY] = event
    if identity:
        query_dict[ALIAS_KEY] = identity
    query_dict.update(properties)
    return urlencode(query_dict)
