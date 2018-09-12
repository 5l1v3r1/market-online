
import os 
from django.conf import settings 

DEBUG = False 


DATABASES = settings.DATABASES 

import dj_database_url 
DATABASES['default'] = dj_database_url.config() 

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https') 

ALLOWED_HOSTS = ['*'] 

SHARE_URL = 'https://127.0.0.1:8000' 
