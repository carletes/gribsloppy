#!/usr/bin/env python

from setuptools import setup, find_packages

import gribsloppy


setup(
    name="gribsloppy",
    version=gribsloppy.__version__,
    description=gribsloppy.__doc__,
    author="Carlos Valiente",
    author_email="carlos@pepelabs.net",
    url="https://github.com/carletes/gribsloppy",

    packages=find_packages(),
    package_data={
        "gribsloppy.test": ["*.grib1"],
    },
    zip_safe=False,
)
