from .base import *

DEBUG = False

ALLOWED_HOSTS = ['ip_address']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': config('DB_NAME'),
        'USERNAME': config('USERNAME'),
        'PASSWORD':config('PASSWORD'),
        'HOST':config('HOST'),
        'PORT':config('PORT')

    }
}