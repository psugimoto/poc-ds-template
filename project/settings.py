#coding: utf-8
# Be prepared for Python2/3
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

import os, sys
import importlib

DJANGO_ENVIRONMENT = os.environ.setdefault('DJANGO_ENVIRONMENT', 'development').strip()
print('Environment detected:', DJANGO_ENVIRONMENT, file=sys.stderr)

SETTINGS_MODULE = __name__.rpartition('.')[0] + '.environments.%s' % DJANGO_ENVIRONMENT
print('Using settings module: "%s"' % SETTINGS_MODULE, file=sys.stderr)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

locals().update(importlib.import_module(SETTINGS_MODULE).__dict__)

print('', file=sys.stderr) # bare newline

