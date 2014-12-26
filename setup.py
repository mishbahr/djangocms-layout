#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import djangocms_layout

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = djangocms_layout.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='djangocms-layout',
    version=version,
    description="""Produce a wonderful columned design in a matter of seconds. Use your own grid system or a prepackaged CSS framework such as Twitter Bootstrap or Foundation Framework. It's a quick, easy & flexible way to create a responsive web site.""",
    long_description=readme + '\n\n' + history,
    author='Mishbah Razzaque',
    author_email='mishbahx@gmail.com',
    url='https://github.com/mishbahr/djangocms-layout',
    packages=[
        'djangocms_layout',
    ],
    include_package_data=True,
    install_requires=[
        'django-appconf',
    ],
    license="BSD",
    zip_safe=False,
    keywords='djangocms-layout',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)