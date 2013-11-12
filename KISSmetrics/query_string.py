# -*- coding: utf-8 -*-

KEY_PARAM = '_k'
PERSON_PARAM = '_p'
EVENT_NAME_PARAM = '_n'
TIME_PARAM = '_t'
TIME_FLAG_PARAM = '_d'
ALIAS_PARAM = '_n'


try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


def create_query(key, person, event=None, timestamp=None,
                 identity=None, properties=None):
    if properties is None:
        properties = {}

    params = {KEY_PARAM: key, PERSON_PARAM: person}
    if timestamp:
        params[TIME_FLAG_PARAM] = 1
        params[TIME_PARAM] = timestamp
    if event:
        params[EVENT_NAME_PARAM] = event
    if identity:
        params[ALIAS_PARAM] = identity
    for key, value in properties.items():
        params[key] = value
    return urlencode(params)
