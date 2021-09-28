#!/bin/bash
version=$(git describe)
python3 setup.py sdist
rm -rf .eggs/
py2dsc-deb dist/exporter_proxy-${version}.tar.gz

