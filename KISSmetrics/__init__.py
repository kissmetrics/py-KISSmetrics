# -*- coding: utf-8 -*-

#: Current URI for all Tracking service endpoints.
TRACKING_HOSTNAME = 'trk.kissmetrics.com'
#: Default protocol for inbound request to the Tracking service.
TRACKING_PROTOCOL = 'http'

#: The URI for the endpoint to record events via the Tracking service.
#:
#: :see: http://support.kissmetrics.com/apis/specifications#recording-an-event
RECORD_URI = 'e'
#: The URI for the endpoint to set a property via the Tracking service.
#:
#: :see: http://support.kissmetrics.com/apis/specifications#setting-properties
SET_URI = 's'
#: The URI for the endpoint that aliases identities performing events via the
#: Tracking service.
#:
#: :see: http://support.kissmetrics.com/apis/specifications#aliasing-users
ALIAS_URI = 'a'

__author__ = 'Ernest W. Durbin III <ewdurbin@gmail.com>'
__license__ = 'MIT'
__version__ = 'develop'

from .client import Client
from .client_compat import ClientCompat
from .client_compat import ClientCompat as KM
from .query_string import QueryString
