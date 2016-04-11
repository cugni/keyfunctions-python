#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
      name='key-functions-python',
      version='1.0',
      description='D8-tree key functions.',
      author='Cesare Cugnasco',
      author_email='cesare.cugnasco@bsc.es',
      long_description=readme,
      url='https://github.com/cugni/key-functions-python',
      license=license,
      packages=find_packages(exclude=('tests', 'docs'))
)

