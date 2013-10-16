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


class QueryString:

    def __init__(self, key, person, event=None, timestamp=None,
                 identity=None, properties={}):
        self.key = key
        self.person = person
        self.event = event
        self.timestamp = timestamp
        self.identity = identity
        self.properties = properties
        self.query_string = self.create_query_string()

    def create_query_string(self):
        params = {KEY_PARAM: self.key,
                  PERSON_PARAM: self.person}
        if self.timestamp:
            params[TIME_FLAG_PARAM] = 1
            params[TIME_PARAM] = self.timestamp
        if self.event:
            params[EVENT_NAME_PARAM] = self.event
        if self.identity:
            params[ALIAS_PARAM] = self.identity
        for key, value in self.properties.items():
            params[key] = value
        return urlencode(params)
