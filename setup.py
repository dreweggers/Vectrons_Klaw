#!/usr/bin/env python
# Our initialization commands and all setup info will go in this file
# This file is crucial to our entire project
#  All important information will end up in the setup() function
#
# We should look at requirement files vs install_requires and see what is best for our dependency needs
# Reference: http://packaging.python.org/distributing/

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

from net import __version__

setup(name='Vectrons_Klaw',
	version=__version__,
	packages=['net'],
	url='https://github.com/dreweggers/Vectrons_Klaw',
	license='MIT',
	author='Drew Eggers, Steve Esswein',
	author_email='sjesswein1s@semo.edu',
	description='Python Project for Network Testing',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Console',
		'Intended Audience :: Education',
		'License :: OSI Approved :: MIT License',
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.5',
		'Topic :: System :: Networking',
	],
	install_requires=[
		'python-pcapy',
	])
