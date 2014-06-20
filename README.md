py-KISSmetrics
==============

[![Build Status](https://travis-ci.org/kissmetrics/py-KISSmetrics.png?branch=master)](https://travis-ci.org/kissmetrics/py-KISSmetrics)
[![Coverage Status](https://coveralls.io/repos/kissmetrics/py-KISSmetrics/badge.png)](https://coveralls.io/r/kissmetrics/py-KISSmetrics)

KISSmetrics tracking API wrapper for Python

Support for:
  - Python 2.6, 2.7, 3.2, 3.3, 3.4

Also tested against:
  - PyPy (Generally the latest release)

Documentation: http://py-kissmetrics.readthedocs.org

## Using this library

```
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

```

## Compatibility client

A compatibility client is provided which is intended to act like the previous generation of Python library [here](https://github.com/kissmetrics/KISSmetrics/blob/master/KISSmetrics/__init__.py)

This interface is provided for compatibility only, and will not be supported in the future.

### Example Usage

```
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

```

## Development setup

```
git clone https://github.com/kissmetrics/py-KISSmetrics.git
cd py-KISSmetrics
virtualenv env
source env/bin/activate
pip install -r test-requirements.txt
py.test
```

### Running Tests

If you'd like to run tests against all of our declared supported Pythons, you can do so using [tox](http://tox.readthedocs.org/en/latest/)

```
pip install tox
tox
```
