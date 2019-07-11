#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

temp_install_reqs = []
install_reqs = []
dependency_links = []

with open("../../requirements.txt", "r") as f:
    temp_install_reqs = list(map(str.strip, f.readlines()))

for req in temp_install_reqs:
    if req.startswith("https://"):
        dependency_links.append(req)
        install_reqs.append(req[req.find("egg=") + 4:].replace("-", "==", 1))
    else:
        install_reqs.append(req)

    name='scraper',
    version='0.0.1',
    description="scraper for private",
    author="yoqp",
    url='https://github.com/yoqp/scraper',
    packages=find_packages(exclude=['tests.*', 'tests']),
    include_package_data=True,
    install_requires=install_reqs,
    dependency_links=dependency_links,
    zip_safe=False,
    keywords='scraper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)