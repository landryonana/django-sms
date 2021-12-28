import os
import django_heroku
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4g&*(wmh_ad1v2hsb&3b46&lrtg437vb2(g9=i6jp4tdmskk+g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    #=====================================================================
    #=================MY APP==============================================
    #============accounts app
    'accounts.apps.AccountsConfig',

    
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    #=====================================================================
    #=================MY LIBRARY==============================================
    'cloudinary_storage',
    'cloudinary',
    'widget_tweaks',
    #'ckeditor',
    #'ckeditor_uploader',
    #=====================================================================
    #=================MY APP==============================================
    #============evangelisation app
    'evangelisation.apps.EvangelisationConfig',
]


SHORT_DATE_FORMAT = 'd/m/Y'

DATE_INPUT_FORMATS = [
    '%d/%m/%Y'
]

TIME_INPUT_FORMATS = [
    '%H:%M',        # '14:30'
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

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd1g7o5pb8smgu2',
        'USER': 'oafftxdxuzrmrn',
        'PASSWORD': '11c8d0367a0b44c2a679280d1156fcd352b988cdda9531802a5b4c4d5031a78e',
        'HOST': 'ec2-54-220-166-184.eu-west-1.compute.amazonaws.com',
        'POST': '5432',
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

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
django_heroku.settings(locals())

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#==============================================================
#==============================================================
#======FILE MANAGER FOR DEV=========
#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
#==============================================================
#==============================================================
#======FILE MANAGER FOR PRODUCT=========
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'vh-cam',
    'API_KEY': '259285251143441',
    'API_SECRET': 'aJvmF3SsffpBJFzVUcF8Bi6JPuM'
}

DEFAULT_FILE_STORAGE='cloudinary_storage.storage.MediaCloudinaryStorage'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
