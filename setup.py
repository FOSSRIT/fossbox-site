#!/bin/env python
# -*- coding: utf8 -*-

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

version = "0.1.0"

setup(
    name="FOSSBox-site",
    version=version,
    description="Website for The FOSSBox at RIT",
    classifiers=[
        "Intended Audience :: Education",
    ],
    keywords="flask mako bootstrap RIT",
    author="Remy DeCausemaker",
    author_email="remyd@civx.us",
    url="http://staging-fossbox.rhcloud.com",
    license="AGPL",
    packages=find_packages(
    ),
    scripts=[
        "distribute_setup.py",
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "flask",
        "flask-mako",
    ],
    #TODO: Deal with entry_points
    #entry_points="""
    #[console_scripts]
    #pythong = pythong.util:parse_args
    #"""
)
