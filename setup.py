#!/usr/bin/env python

from distutils.core import setup

import os
import re

base_path = os.path.dirname(__file__)

fp = open(os.path.join(base_path, 'KISSmetrics', '__init__.py'))
VERSION = re.compile(r".*__version__ = '(.*?)'",
                     re.S).match(fp.read()).group(1)
fp.close()


version = VERSION

requirements = ['urllib3']
tests_requirements = ['pytest']

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
      requires=requirements,
      tests_require=tests_requirements,
      )
