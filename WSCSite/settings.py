"""
Django settings for WSCSite project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import ldap3

#ldap
#import ldap
#from django_auth_ldap.config import LDAPSearch, GroupOfNamesType


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6xt*t1ifew*hvsyyl+z=l2+1jl%cuu#z26yldi8nwlx(^#gg(k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'message_board.apps.MessageBoardConfig',
    'main.apps.MainConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # custom user model
    'users.apps.UsersConfig',
    'administration.apps.AdministrationConfig',
    'user_message_board.apps.UserMessageBoardConfig', # Only here to be used in testing...

    # my app
    'WSCSite',
]

AUTH_USER_MODEL = 'users.CustomUser'

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'WSCSite.middleware.login_required_middleware.LoginRequiredMiddleware', # Doesn't work -> Fix
]

ROOT_URLCONF = 'WSCSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'WSCSite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
    # ,
    # 'lamp': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'database',
    #     'USER': 's1748323',
    #     'PASSWORD': 's1748323',
    #     'HOST': '146.141.21.92',
    #     'PORT': '22',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

# NOTE: Remember to put this back in for actual product - Just for testing
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# Tries these backends in order until one works
AUTHENTICATION_BACKENDS = (
    # 'django_auth_ldap.backend.LDAPBackend',  # Will try ldap first, if it doesn't work will try default backend
    # 'utils.witsldapauth.LDAPBackendWitsStudents',  # Should use file as backend... hopefully
    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'  # change to right timezone

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/Admin_message_board/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

#  list of folders where Django will search for additional static files
#  aside from the static folder of each app installed
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# redirect for successful login
# LOGIN_REDIRECT_URL = '/admin/'
