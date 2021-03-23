from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = ['oloproject.eba-mdgm24am.us-west-2.elasticbeanstalk.com']
SECRET_KEY = os.environ('SECRET_KEY')
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('RDS_DB_NAME'),
#         'USER': os.environ.get('RDS_USERNAME'),
#         'PASSWORD': os.environ.get('RDS_PASSWORD'),
#         'HOST': os.environ.get('RDS_HOSTNAME'),
#         'PORT': os.environ.get('RDS_PORT')
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)
