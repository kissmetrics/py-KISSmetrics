TRACKING_HOSTNAME = 'trk.kissmetrics.com'
TRACKING_PROTOCOL = 'http'

RECORD_PATH = 'e'
SET_PATH = 's'
ALIAS_PATH = 'a'

__author__ = 'Ernest W. Durbin III <ewdurbin@gmail.com>'
__license__ = 'MIT'
__version__ = 'develop'

from .client import Client
from .client_compat import ClientCompat
from .client_compat import ClientCompat as KM
