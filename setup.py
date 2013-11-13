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

install_reqs = parse_requirements(os.path.join(base_path, 'requirements.txt'))
test_reqs = parse_requirements(os.path.join(base_path, 'test-requirements.txt'))

requirements = [str(ir.req) for ir in install_reqs]
test_requirements = [str(ir.req) for ir in test_reqs]

version = VERSION

setup(name='KISSmetrics',
      version=version,
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
      license='MIT',
      packages=['KISSmetrics'],
      install_requires=requirements,
      tests_require=test_requirements,
      )
