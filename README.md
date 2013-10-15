py-KISSmetrics
==============

KISSmetrics tracking API wrapper for Python

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
py.test --cov KISSmetrics/
```
