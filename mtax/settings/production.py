from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
  'mta-x.net',
  'mta-x.herokuapp.com'
]

DATABASES = {
  'default': {}
}

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Use Amazon S3 bucket for static files
STATIC_URL = 'https://s3.amazonaws.com/mta-x/'