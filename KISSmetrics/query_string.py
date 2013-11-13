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
    if properties is None:
        properties = {}

    query_dict = {KEY_KEY: key, PERSON_KEY: person}
    if timestamp:
        query_dict[TIME_FLAG_KEY] = 1
        query_dict[TIME_KEY] = timestamp
    if event:
        query_dict[EVENT_NAME_KEY] = event
    if identity:
        query_dict[ALIAS_KEY] = identity
    query_dict.update(properties)
    return urlencode(query_dict)
