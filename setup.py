#!/usr/bin/python
# -*- coding: utf-8 -*-

# Facilis

from setuptools import setup, find_packages

print find_packages()

setup(
    name = "Facilis",
    version = "0.1",
    packages = find_packages(),
    install_requires = ['PyYaml'],
    scripts = ['facilis.py'],
    author = "João Moreno",
    author_email = "alph.pt@gmail.com",
    description = "Send files through HTTP without hassle.",
    license = "GPL",
    keywords = "facilis share http hassle"
)
