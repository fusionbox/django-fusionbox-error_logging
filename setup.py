#!/usr/bin/env python
import os
import re
from setuptools import setup, find_packages

__doc__="""
Improved Broken Link emailing and logging
"""

version = '0.0.1'

setup(name='django-fusionbox-error_logging',
    version=version,
    description='Reusable Contact Form application for Django',
    author='Fusionbox programmers',
    author_email='programmers@fusionbox.com',
    keywords='django error_logging',
    long_description=__doc__,
    url='https://github.com/fusionbox/django-fusionbox-error_logging',
    packages=find_packages(),
    namespace_packages=['fusionbox'],
    platforms = "any",
    license='BSD',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
    install_requires = ['django_fusionbox'],
    requires = ['django_fusionbox'],
)

