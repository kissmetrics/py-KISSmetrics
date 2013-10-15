# -*- coding: utf-8 -*-

RECORD_URI = '/e'
SET_URI = '/t'
ALIAS_URI = '/a'

KEY_PARAM = '_k'
PERSON_PARAM = '_p'
EVENT_NAME_PARAM = '_n'
TIME_PARAM = '_t'
TIME_FLAG_PARAM = '_d'
ALIAS_PARAM = '_n'


from urllib import urlencode


class Request:

    def __init__(self, key, person, event=None, timestamp=None,
                 alias=None, properties={}):
        self.key = key
        self.person = person
        self.event = event
        self.timestamp = timestamp
        self.alias = alias
        self.properties = properties

    @property
    def query_string(self):
        params = {KEY_PARAM: self.key,
                  PERSON_PARAM: self.person}
        if self.timestamp:
            params[TIME_FLAG_PARAM] = 1
            params[TIME_PARAM] = self.timestamp
        if self.event:
            params[EVENT_NAME_PARAM] = self.event
        if self.alias:
            params[ALIAS_PARAM] = self.alias
        return urlencode(params)


def record(key, person, event, timestamp=None, properties={}):
    pass


def set(key, person, timestamp=None, properties={}):
    pass


def alias(key, person, identity):
    pass
