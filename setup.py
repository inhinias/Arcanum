#!/usr/bin/env python3
import os
import sys
from setuptools import setup

if sys.version_info < (3, 5):
    sys.exit('Python 3.5 is required to run arcanum')

data_files = []

for directory, _, filenames in os.walk(u'share'):
    dest = directory[6:]
    if filenames:
        files = []
        for filename in filenames:
            filename = os.path.join(directory, filename)
            files.append(filename)
        data_files.append((os.path.join('share', dest), files))


setup(
    name='arcanum',
    version='0.0.1',
    license='GPL-3',
    author='JFK422',
    author_email='galenite@protonmail.com',
    packages=['arcanum', 'arcanum.components', 'arcanum.components.uiElements', 'arcanum.components.uiElements.tabs'],
    data_files=data_files,
    install_requires=[
        'mysql-connector',
        'PyQt5',
        'PyQt5-sip',
        'python-gnupg',
        'QtAwesome',
        'QtPy',
        'six'
    ],
    url='https://github.com/JFK422/Arcanum/',
    description='An encryption manager',
    long_description="""Arcanum is a tool for handling encryption. Generate/store passwords in a database
    of your choice.
    Handle keys and asymmetric stuff.
    STILL IN THE WORKS!""",
    classifiers=[
        #3 - Alpha
        #4 - Beta
        #5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Operating System :: Linux',
        'Topic :: Office/Business'
    ],
)
