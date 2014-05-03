#!/usr/bin/env python
from setuptools import setup
from os import path

setup(
    name = 'bambu-sites',
    version = '0.1',
    description = 'Middleware that redirects users to a site\'s primary domain, based on the `django.contrib.sites` framework',
    author = 'Steadman',
    author_email = 'mark@steadman.io',
    url = 'https://github.com/iamsteadman/bambu-sites',
    long_description = open(path.join(path.dirname(__file__), 'README')).read(),
    install_requires = ['Django>=1'],
    packages = ['bambu_sites'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django'
    ]
)
