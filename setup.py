#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="ethereum-dasm",
    version="0.2",
    packages=find_packages(),
    author="tintinweb",
    author_email="tintinweb@oststrom.com",
    description=(
        "An ethereum bytecode disassembler with static and dynamic analysis features"),
    license="GPLv2",
    keywords=["ethereum", "blockchain", "evm", "disassembler"],
    url="https://github.com/tintinweb/ethereum-dasm",
    download_url="https://github.com/tintinweb/ethereum-dasm/tarball/v0.1",
    #python setup.py register -r https://testpypi.python.org/pypi
    long_description=read("README.rst") if os.path.isfile("README.rst") else read("README.md"),
    install_requires=["colorama",
                      "requests",
                      "tabulate"],
    #package_data={},
    extras_require={"mythril": ["mythril"],  # for laser-ethereum
                    "abidecoder": ["ethereum-input-decoder", "pyetherchain"],},
)