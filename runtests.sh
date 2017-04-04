#!/usr/bin/env sh
pip install -r requirements-test.txt
py.test -v -s --cov --cov-report=term-missing --cov-report=html
