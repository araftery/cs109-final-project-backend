from base import *

############################################################
##### STATIC FILES #########################################
############################################################

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

############################################################
##### OTHER ################################################
############################################################

DEBUG = False
TEMPLATE_DEBUG = False

SETTINGS_MODULE = 'settings.prod_heroku'
