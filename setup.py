import os
import multiprocessing
import time
import random                       # for coming up with random numbers
from multiprocessing import Pool    # for pooling answers
from setuptools import setup, find_packages
# from primefinders.toolkit import convert


# LONG_DESCRIPTION = convert("README.md")

setup(name='primefinders',
      version='0.0.1',
      description='Python library identifying prime numbers',
      long_description=LONG_DESCRIPTION,
      author='LaGuer',
      url='https://github.com/LaGuer/PrimeFinders',
      license='GNU General Public License v3.0',
      tests_require=['pytest'],
      install_requires=['matplotlib>=2.1'],
      keywords=['prime',
                'fermat',
                'euler',
                'galois',
                'miller',
                'poincare',
                'riemann',
                'math'],
      packages=find_packages(),
      package_data={
          'License': ['LICENSE'],
          'Readme': ['README.md'],
      },
      platforms='any',
      zip_safe=False,
      test_suite='tests.test_primefinders',
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3.6",
          "Environment :: Other Environment",
          "Intended Audience :: Developers",
          "Intended Audience :: Science/Research",
          "Intended Audience :: Education",
          "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
          "Operating System :: OS Independent",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Software Development :: Libraries",
          "Topic :: Scientific/Engineering :: Mathematics",
          "Topic :: Utilities"]
      )
