from uni_db.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'unimax',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

