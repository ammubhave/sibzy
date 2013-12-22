from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sibzy',
	'OPTIONS': {
            'read_default_file': '/home/ubuntu/.my.cnf',
        },
    }
}


ALLOWED_HOSTS = ("sibzy.com", "localhost", "www.sibzy.com", "127.0.0.1", )
