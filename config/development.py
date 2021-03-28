from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = ['oloproject.eba-mdgm24am.us-west-2.elasticbeanstalk.com']
SECRET_KEY = os.environ['SECRET_KEY']
# SECRET_KEY = '=+zl2)zrcv=dduc1@bw)+ab)6x8)97nm**i!vruv)oal@$y4&!'
if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)
STATIC_ROOT = 'static'