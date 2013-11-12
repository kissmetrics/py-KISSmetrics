# -*- coding: utf-8 -*-

TRACKING_HOSTNAME = 'trk.kissmetrics.com'
TRACKING_PROTOCOL = 'http'

RECORD_URI = 'e'
SET_URI = 's'
ALIAS_URI = 'a'

__author__ = 'Ernest W. Durbin III <ewdurbin@gmail.com>'
__license__ = 'MIT'
__version__ = 'develop'

from .client import Client
from .client_compat import ClientCompat
from .client_compat import ClientCompat as KM
