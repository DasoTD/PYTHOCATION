import os

# from apt import Cache
from .base import *


DEBUG = False

ADMINS = [
    ('David D', 'dasodavid4@gmail.com'),
]

# ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']
ALLOWED_HOSTS = ['*']

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.environ.get('POSTGRES_DB'),
       'USER': os.environ.get('POSTGRES_USER'),
       'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
       'HOST': 'db',
       'PORT': 5432,
   }
}

# REDIS_URL = 'redis://cache:6379'
# Cache['default']['LOCATION'] = REDIS_URL
# CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]

# # Security
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True