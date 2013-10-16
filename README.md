py-KISSmetrics
==============

**WARNING: Still under active development, do not use this in Production**

[![Build Status](https://travis-ci.org/kissmetrics/py-KISSmetrics.png?branch=master)](https://travis-ci.org/kissmetrics/py-KISSmetrics)
[![Coverage Status](https://coveralls.io/repos/kissmetrics/py-KISSmetrics/badge.png)](https://coveralls.io/r/kissmetrics/py-KISSmetrics)

**Again, this is NOT ready for Production use.**

KISSmetrics tracking API wrapper for Python

Support for:
  - Python 2.6, 2.7, 3.2, 3.3
  - pypy 1.9

## Using this library

```
>>> import KISSmetrics
>>> KM = KISSmetrics.Client(key='mySuperSecretApiKey')
>>> KM.record('bob@bob.com', 'Viewed Homepage')
<urllib3.response.HTTPResponse object at 0x109f2c890>
>>> KM.record('bob@bob.com', 'Signed Up', {'Plan' : 'Pro', 'Amount' : 99.95})
<urllib3.response.HTTPResponse object at 0x109f2ca50>
>>> KM.record('bob@bob.com', 'Signed Up', timestamp=1234567890)
<urllib3.response.HTTPResponse object at 0x109f2c910>
>>> KM.set('bob@bob.com', {'gender': 'male'})
<urllib3.response.HTTPResponse object at 0x109f2c750>
```

## Development setup

```
git clone https://github.com/kissmetrics/py-KISSmetrics.git
cd py-KISSmetrics
virtualenv env
source env/bin/activate
pip install -r requirements.txt
pip install -r test-requirements.txt
py.test --cov KISSmetrics/
```
