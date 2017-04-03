from .development import *

print >> sys.stderr, "/!\ USING TEST ENVIRONMENT /!\ "

DEBUG = True
TEMPLATE_DEBUG = DEBUG

TEMPLATES[0]['OPTIONS']['debug'] = TEMPLATE_DEBUG; del TEMPLATE_DEBUG

import dj_database_url
DATABASES['default'] = dj_database_url.config(default='sqlite:///' + os.path.join(BASE_DIR, 'db_test.sqlite3'))

