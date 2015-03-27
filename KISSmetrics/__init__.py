# -*- coding: utf-8 -*-

#: Default host for tracking service endpoint
TRACKING_HOSTNAME = 'trk.kissmetrics.com'

#: Default scheme for requests to tracking service endpoint
TRACKING_SCHEME = 'http'

#: Path to record events via tracking service
#:
#: .. seealso:: http://support.kissmetrics.com/apis/specifications#recording-an-event
RECORD_PATH = 'e'

#: Path to set a property via tracking service
#:
#: .. seealso:: http://support.kissmetrics.com/apis/specifications#setting-properties
SET_PATH = 's'

#: Path to alias two identities via tracking service
#:
#: .. seealso:: http://support.kissmetrics.com/apis/specifications#aliasing-users
ALIAS_PATH = 'a'

__author__ = 'Ernest W. Durbin III <ewdurbin@gmail.com>'
__license__ = 'MIT'
__version__ = '1.0.1'

from .client import Client
from .client_compat import ClientCompat
from .client_compat import ClientCompat as KM
