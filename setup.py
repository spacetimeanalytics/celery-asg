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
      entry_points={
          'console_scripts': [
              'celery-asg = celeryasg.cli:entrypoint'
          ]
      })
