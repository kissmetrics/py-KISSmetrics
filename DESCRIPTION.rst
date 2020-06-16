py-KISSmetrics
--------------

KISSmetrics tracking API wrapper for Python

A description of the API can be found at: https://support.kissmetrics.io/reference#api-specifications-1

Support for:
  - Python 2.6, 2.7, 3.2, 3.3

Also tested against:
  - PyPy (Generally the latest release)

Documentation: http://py-kissmetrics.readthedocs.org/


Using this library
==================

>>> import KISSmetrics
>>> KM = KISSmetrics.Client(key='mySuperSecretApiKey')
>>> KM.record('bob@bob.com', 'Viewed Homepage')
<urllib3.response.HTTPResponse object at 0x...>
>>> KM.record('bob@bob.com', 'Signed Up', {'Plan' : 'Pro', 'Amount' : 99.95})
<urllib3.response.HTTPResponse object at 0x...>
>>> KM.record('bob@bob.com', 'Signed Up', timestamp=1234567890)
<urllib3.response.HTTPResponse object at 0x...>
>>> KM.set('bob@bob.com', {'gender': 'male'})
<urllib3.response.HTTPResponse object at 0x...>



Compatibility client
====================

A compatibility client is provided which is intended to act like the previous generation of Python library here_.

This interface is provided for compatibility only, and will not be supported in the future.

Example Usage
+++++++++++++

>>> from KISSmetrics import KM
>>> km = KM("this is your API key")
>>> km.key
'this is your API key'
>>> km.identify('bob@bob.com')
>>> km.identity
'bob@bob.com'
>>> km.check_id_key() # this will throw exception if key or identity is None
>>> km.record('Viewed Homepage')
>>> km.record('Signed Up', {'Plan' : 'Pro', 'Amount' : 99.95})
>>> km.record('Signed Up', {'_d' : 1, '_t' : 1234567890})
>>> km.set({'gender' : 'male'})


.. _here: https://github.com/kissmetrics/KISSmetrics/blob/master/KISSmetrics/__init__.py


