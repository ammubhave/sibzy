from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ON_SERVER = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sibzy',
	'OPTIONS': {
            'read_default_file': '~/.my.cnf',
        },
    }
}

import sys
if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}


INSTALLED_APPS += ("debug_toolbar", )
INTERNAL_IPS = ("127.0.0.1",)

MIDDLEWARE_CLASSES += ("debug_toolbar.middleware.DebugToolbarMiddleware", )

