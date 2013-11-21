#!/usr/bin/env python

from setuptools import setup

import os
import re

base_path = os.path.dirname(__file__)

fp = open(os.path.join(base_path, 'KISSmetrics', '__init__.py'))
VERSION = re.compile(r".*__version__ = '(.*?)'",
                     re.S).match(fp.read()).group(1)
fp.close()

version = VERSION

def read(fname):
    try:
        path = os.path.join(os.path.dirname(__file__), fname)
        return open(path).read()
    except IOError:
        return ""

requirements =      ['urllib3==1.7.1']
test_requirements = ['pytest',
                     'pytest-cov']

setup(
    name='py-KISSmetrics',
    version=version,
    license='MIT',
    description="Official KISSmetrics client library.",
    long_description=read('README.md'),
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='',
    author='Ernest W. Durbin III',
    author_email='ewdurbin@gmail.com',
    url='https://github.com/kissmetrics/py-KISSmetrics/',
    packages=['KISSmetrics'],
    test_suite='KISSmetrics.tests',
    install_requires=requirements,
    tests_require=test_requirements,
)
