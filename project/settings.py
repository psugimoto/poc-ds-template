#coding: utf-8
import os, sys
import importlib

DJANGO_ENVIRONMENT = os.environ.setdefault('DJANGO_ENVIRONMENT', 'development').strip()
print >> sys.stderr, 'Environment detected:', DJANGO_ENVIRONMENT

SETTINGS_MODULE = __name__.rpartition('.')[0] + '.environments.%s' % DJANGO_ENVIRONMENT
print >> sys.stderr, 'Using settings module: "%s"' % SETTINGS_MODULE

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

locals().update(importlib.import_module(SETTINGS_MODULE).__dict__)

print >> sys.stderr, '' # bare newline

