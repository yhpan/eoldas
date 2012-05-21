from setuptools import setup, find_packages
import sys, os

version = '1.0'
DISTNAME = "eoldas"
DESCRIPTION = "An Earth Observation Land Data Assimilation System (EO-LDAS)"
LONG_DESCRIPTION = open('README.rst').read()
MAINTAINER = 'Jose Gomez-Dans/NCEO & University College London'
MAINTAINER_EMAIL = "j.gomez-dans@ucl.ac.uk"
URL = 'http://github.com/jgomezdans/eoldas'
LICENSE = 'Undecided'
VERSION = "1.0.1"
DOWNLOAD_URL="https://github.com/jgomezdans/semidiscrete/zipball/master"

setup(name='eoldas',
      version=version,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      url='http://www.assimila.eu/eoldas',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          # It require the RT codes, but the package names are still in flux
          ],
          classifiers=[
              'Intended Audience :: Science/Research',
              'Intended Audience :: Developers',
              'License :: OSI Approved',
              'Programming Language :: Fortran',
              'Programming Language :: Python',
              'Topic :: Software Development',
              'Topic :: Scientific/Engineering',
              'Operating System :: Microsoft :: Windows',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS'
              ],
      )
