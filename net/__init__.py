#!/usr/bin/env python
# We will add our module imports here in the future

from collections import namedtuple

__version_info__ = namedtuple(
    'version_info',
    'major minor micro releaselevel serial')(major=0,
                                             minor=0,
                                             micro=1,
                                             releaselevel='alpha',
                                             serial=0)

__version__ = '{v.major}.{v.minor}.{v.micro}'.format(v=__version_info__)
