from .base import *

DEBUG = False

ALLOWED_HOSTS = ['ip_address']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'DB Name',
        'USERNAME':'',
        'PASSWOIRD':'',
        'HOST':'',
        'PORT':''

    }
}