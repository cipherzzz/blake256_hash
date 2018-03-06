# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="blake256_hash",
    version="0.1.0",
    description="A Python module supporting blake256 hashing",
    license="MIT",
    author="cipherZ",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ]
)
