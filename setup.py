#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TODO
"""

from distutils.core import setup

setup(name='Celery ASG',
      version='0.1.0',
      description=__doc__,
      author='Erle Carrara',
      author_email='carrara.erle@gmail.com',
      url='https://github.com/spacetimeanalytics/asg-manager',
      packages=['celeryasg'],
      install_requires=[
        'amqp>=2.2.2',
        'billiard>=3.5.0.3',
        'boto3>=1.6.3',
        'botocore>=1.9.3',
        'celery>=4.1.0',
        'docopt>=0.6.2',
        'kombu>=4.1.0',
        'py>=1.5.2',
        'python-dateutil>=2.6.1',
        'pytz>=2018.3',
        's3transfer>=0.1.13',
      ],
      entry_points={
          'console_scripts': [
              'celery-asg = celeryasg.cli:entrypoint'
          ]
      })
