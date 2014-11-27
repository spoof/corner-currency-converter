#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Dirty hack to prevent ``python setup.py sdist`` from making hard links:
# it doesn't work in VMWare/VBox shared folders.
import os
del os.link

install_requires = [
    'Flask==0.10.1',
    'Flask-WTF==0.10.3'
]

setup(
    name='cornerapp-currency-converter',
    version='0.1',
    license='BSD',
    description='HTTP service for currency converting',
    long_description=__doc__,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    packages=['currency_converter'],
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False,
    platforms='any'
)
