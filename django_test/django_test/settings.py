"""
Django settings for django_test project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qims_k3wzr@kihbn5whi5je&)0=7s=2j$bo!r_%@nv0mrqu(kw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sample',
    'django_saml'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_test.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'django_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


AUTH_USER_MODEL = 'sample.TestUser'

LOGIN_URL = '/saml/login'

APPEND_SLASH = True

SAML_SP = {
    "entityId": "http://127.0.0.1:8000/saml/metadata/",
    "assertionConsumerService": {
        "url": "http://127.0.0.1:8000/saml/acs/",
        "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"
    },
    "singleLogoutService": {
        "url": "http://127.0.0.1:8000/saml/sls/",
        "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"
    },
    "NameIDFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified"
}

SAML_BASE_DIRECTORY = BASE_DIR

SAML_IDP_URL = 'http://192.168.99.100:8080/simplesaml/saml2/idp/metadata.php'

SAML_SECURITY = {
    "nameIdEncrypted": False,
    "authnRequestsSigned": True,
    "logoutRequestSigned": True,
    "logoutResponseSigned": False,
    "signMetadata": False,
    "wantMessagesSigned": False,
    "wantAssertionsSigned": False,
    "wantNameId": True,
    "wantNameIdEncrypted": False,
    "wantAssertionsEncrypted": False,
    "signatureAlgorithm": "http://www.w3.org/2000/09/xmldsig#rsa-sha1",
    "digestAlgorithm": "http://www.w3.org/2000/09/xmldsig#sha1"
}

SAML_CONTACT = {
    "technical": {
        "givenName": "Technology Director",
        "emailAddress": "technology@thon.org"
    },
    "support": {
        "givenName": "Lead Systems Admin",
        "emailAddress": "systems@thon.org"
    }
}

SAML_USERNAME_ATTR = 'email'

SAML_ATTR_MAP = [
    ('email', 'email')
]

AUTHENTICATION_BACKENDS = [
    'django_test.backends.CustomSamlBackend'
]
