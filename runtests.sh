#!/usr/bin/env sh
pip install -r requirements-test.txt
DJANGO_ENVIRONMENT=test py.test -v -s --cov --cov-report=term-missing --cov-report=html
