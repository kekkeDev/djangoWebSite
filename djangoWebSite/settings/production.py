from .base import *

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['*']

import dj_database_url

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
db_from_env = dj_database_url.config()
DATABASES = {
    'default': db_from_env
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'hvcrpasiw',
    'API_KEY': '332695448691772',
    'API_SECRET': 'JgOVlFYvjU6IlppQR65ylBxs2Q0'
}