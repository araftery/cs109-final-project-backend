import os

from path import path

############################################################
##### SETUP ################################################
############################################################

# i.e., where root urlconf is
PROJECT_ROOT = path(__file__).abspath().dirname().dirname()


############################################################
##### DATABASE #############################################
############################################################

ALLOWED_HOSTS = ['*']

############################################################
##### APPS #################################################
############################################################

# Application definition
DEFAULT_APPS = (
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',)

MY_APPS = (
    'core',
)

THIRD_PARTY_APPS = (
    'corsheaders',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + MY_APPS

############################################################
##### MIDDLEWARE ###########################################
############################################################

DEFAULT_MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

THIRD_PARTY_MIDDLEWARE = (
    'bugsnag.django.middleware.BugsnagMiddleware',
)

MIDDLEWARE_CLASSES = DEFAULT_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE

############################################################
##### INTERNATIONALIZATION #################################
############################################################

LANGUAGE_CODE = 'en-us'
USE_I18N = False
USE_L10N = False
INTERNAL_IPS = ['*']

############################################################
##### TEMPLATES ############################################
############################################################

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates').replace('\\','/'),
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as DEFAULT_TCP

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
) + DEFAULT_TCP


############################################################
##### AUTHENTICATION #######################################
############################################################

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
URL_PATH = ''

############################################################
##### STATIC FILES #########################################
############################################################

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static_common').replace('\\','/'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


############################################################
##### OTHER ################################################
############################################################

ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'
SECRET_KEY = 'ye#fx+lsp5sm@4lg@ld(55d64qydp1%=2)wdpa!twr5_827g8n'
DATABASES = {}
TIME_ZONE = 'America/New_York'
SITE_ID = 1

BUGSNAG = {
  "api_key": os.environ.get('BUGSNAG_API_KEY'),
  "project_root": "/app",
}

CORS_ORIGIN_ALLOW_ALL = True
