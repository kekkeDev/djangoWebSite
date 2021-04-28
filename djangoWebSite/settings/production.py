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

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_STORAGE_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_STORAGE_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_STORAGE_API_SECRET')
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
