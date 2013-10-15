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
        self.query_string = self.create_query_string()

    def create_query_string(self):
        params = {KEY_PARAM: self.key,
                  PERSON_PARAM: self.person}
        if self.timestamp:
            params[TIME_FLAG_PARAM] = 1
            params[TIME_PARAM] = self.timestamp
        if self.event:
            params[EVENT_NAME_PARAM] = self.event
        if self.alias:
            params[ALIAS_PARAM] = self.alias
        for key, value in self.properties.items():
            params[key] = value
        return urlencode(params)


def record(key, person, event, timestamp=None, properties={}):
    request = Request(key, person, event=event, timestamp=timestamp,
                      properties=properties)
    return request.query_string


def set(key, person, timestamp=None, properties={}):
    request = Request(key, person, timestamp=timestamp,
                      properties=properties)
    return request.query_string


def alias(key, person, identity):
    request = Request(key, person, identity=identity)
    return request.query_string
