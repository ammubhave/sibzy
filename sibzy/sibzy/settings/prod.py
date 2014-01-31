from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ON_SERVER = True


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
