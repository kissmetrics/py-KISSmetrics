#!/usr/bin/env python

from distutils.core import setup
from pip.req import parse_requirements

import os
import re

base_path = os.path.dirname(__file__)

fp = open(os.path.join(base_path, 'KISSmetrics', '__init__.py'))
VERSION = re.compile(r".*__version__ = '(.*?)'",
                     re.S).match(fp.read()).group(1)
fp.close()

REQS_PATH = os.path.join(base_path, 'requirements.txt')
TEST_REQS_PATH = os.path.join(base_path, 'test-requirements.txt')

install_reqs = parse_requirements(REQS_PATH)
test_reqs = parse_requirements(TEST_REQS_PATH)

requirements = [str(ir.req) for ir in install_reqs]
test_requirements = [str(ir.req) for ir in test_reqs]

version = VERSION

setup(
    name='py-KISSmetrics',
    version=version,
    license='MIT',
    description="Official KISSmetrics client library.",
    long_description="",
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
    install_requires=requirements,
    tests_require=test_requirements,
)
