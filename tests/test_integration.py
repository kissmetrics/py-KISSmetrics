import pytest
import json

import KISSmetrics


class TestKISSmetricsClientIntegration(object):

    def setup(self):
        self.client = KISSmetrics.Client(key='foo', trk_host='httpbin.org')

    def test_record_success(self):
        response = self.client.record(person='bob', event='fizzed', path='get')
        assert response.status == 200

    def test_record_key(self):
        response = self.client.record(person='bob', event='fizzed', path='get')
        data = json.loads(response.data.decode())
        assert data['args']['_k'] == 'foo'

    def test_record_person(self):
        response = self.client.record(person='bob', event='fizzed', path='get')
        data = json.loads(response.data.decode())
        assert data['args']['_p'] == 'bob'

    def test_record_event(self):
        response = self.client.record(person='bob', event='fizzed', path='get')
        data = json.loads(response.data.decode())
        assert data['args']['_n'] == 'fizzed'

    def test_set_success(self):
        response = self.client.set(person='bob', properties={'cool': 1}, path='get')
        assert response.status == 200

    def test_set_key(self):
        response = self.client.set(person='bob', properties={'cool': 1}, path='get')
        data = json.loads(response.data.decode())
        assert data['args']['_k'] == 'foo'

    def test_set_person(self):
        response = self.client.set(person='bob', properties={'cool': 1}, path='get')
        data = json.loads(response.data.decode())
        assert data['args']['_p'] == 'bob'

    def test_set_property(self):
        response = self.client.set(person='bob', properties={'cool': 1}, path='get')
        data = json.loads(response.data.decode())
        assert data['args']['cool'] == '1'

    def test_alias_success(self):
        response = self.client.alias(person='bob', identity='shadybob', path='get')
        assert response.status == 200

    def test_alias_person(self):
        response = self.client.alias(person='bob', identity='shadybob', path='get')
        data = json.loads(response.data.decode())
        assert data['args']['_n'] == 'shadybob'


class TestKISSmetricsClientCompatIntegration(object):

    def setup(self):
        self.client = KISSmetrics.ClientCompat(key='foo', host='httpbin.org:80')

    def test_record_success(self):
        self.client.identify('bob')
        response = self.client.record('fizzed', path='get', resp=True)
        assert response.status == 200

    def test_record_key(self):
        self.client.identify('bob')
        response = self.client.record('fizzed', path='get', resp=True)
        data = json.loads(response.data.decode())
        assert data['args']['_k'] == 'foo'

    def test_record_person(self):
        self.client.identify('bob')
        response = self.client.record('fizzed', path='get', resp=True)
        data = json.loads(response.data.decode())
        assert data['args']['_p'] == 'bob'

    def test_record_event(self):
        self.client.identify('bob')
        response = self.client.record('fizzed', path='get', resp=True)
        data = json.loads(response.data.decode())
        assert data['args']['_n'] == 'fizzed'

    def test_set_success(self):
        self.client.identify('bob')
        response = self.client.set({'cool': 1}, path='get', resp=True)
        assert response.status == 200

    def test_set_key(self):
        self.client.identify('bob')
        response = self.client.set({'cool': 1}, path='get', resp=True)
        data = json.loads(response.data.decode())
        assert data['args']['_k'] == 'foo'

    def test_set_person(self):
        self.client.identify('bob')
        response = self.client.set({'cool': 1}, path='get', resp=True)
        data = json.loads(response.data.decode())
        assert data['args']['_p'] == 'bob'

    def test_set_property(self):
        self.client.identify('bob')
        response = self.client.set({'cool': 1}, path='get', resp=True)
        data = json.loads(response.data.decode())
        assert data['args']['cool'] == '1'

    def test_alias_success(self):
        self.client.identify('bob')
        response = self.client.alias('bob', 'shadybob', path='get', resp=True)
        assert response.status == 200

    def test_alias_person(self):
        self.client.identify('bob')
        response = self.client.alias('bob', 'shadybob', path='get', resp=True)
        data = json.loads(response.data.decode())
        assert data['args']['_n'] == 'shadybob'
