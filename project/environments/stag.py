from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'remembertochangethestagingsecretkeytoo'

TEMPLATES[0]['OPTIONS']['debug'] = TEMPLATE_DEBUG; del TEMPLATE_DEBUG

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

