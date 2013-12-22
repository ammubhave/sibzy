"""
WSGI config for sibzy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
import site

site.addsitedir('/home/ubuntu/.virtualenvs/sibzy/lib/python2.7/site-packages')

path = '/home/ubuntu/sibzy/sibzy'
if path not in sys.path:
    sys.path.append(path)


os.environ.setdefault("SECRET_KEY", "sdfkj234#$%#$%sdfgkjhAASDFSD$53453")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sibzy.settings.dev")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
