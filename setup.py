#!/usr/bin/env python
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "requirements.txt")) as f:
    requirements = f.read().split()


setup(
    name="neuralpredictors",
    version="0.2.0",
    description="Sinz Lab Neural System Identification Utilities",
    author="Sinz Lab",
    author_email="software@sinzlab.net",
    url="https://github.com/sinzlab/neuralpredictors",
    packages=find_packages(exclude=[]),
    install_requires=requirements,
)
