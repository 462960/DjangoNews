from .base import *

DEBUG = os.environ.get('DEBUG_MODE', 'NO') == 'YES'

SECRET_KEY = os.environ.get('SECRET_KEY', '')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 25))
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', 'NO') == 'YES'
