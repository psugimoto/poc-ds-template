from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

TEMPLATES[0]['OPTIONS']['debug'] = TEMPLATE_DEBUG; del TEMPLATE_DEBUG

ALLOWED_HOSTS = ['*']

import dj_database_url
DATABASES['default'] =  dj_database_url.config(default='sqlite:///' + os.path.join(BASE_DIR, 'db_development.sqlite3'))

