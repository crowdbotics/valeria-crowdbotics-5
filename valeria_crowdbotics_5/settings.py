Line Line """

Line 

Line Line Django settings for valeria_crowdbotics_5 project.

Line 

Line Line 

Line 

Line Line Generated by 'django-admin startproject' using Django 1.11.5.

Line 

Line Line 

Line 

Line Line For more information on this file, see

Line 

Line Line https://docs.djangoproject.com/en/1.11/topics/settings/

Line 

Line Line 

Line 

Line Line For the full list of settings and their values, see

Line 

Line Line https://docs.djangoproject.com/en/1.11/ref/settings/

Line 

Line Line """

Line 

Line Line 

Line 

Line Line import os

Line 

Line Line 

Line 

Line Line # Build paths inside the project like this: os.path.join(BASE_DIR, ...)

Line 

Line Line BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Line 

Line Line 

Line 

Line Line 

Line 

Line Line # Quick-start development settings - unsuitable for production

Line 

Line Line # See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

Line 

Line Line 

Line 

Line Line # SECURITY WARNING: keep the secret key used in production secret!

Line 

Line Line SECRET_KEY = '((1q0=er!jzniwq*@6**@=0h2%dz(an#cb=+kbd_8jmyltcl^o'

Line 

Line Line 

Line 

Line Line # SECURITY WARNING: don't run with debug turned on in production!

Line 

Line Line DEBUG = True

Line 

Line Line 

Line 

Line Line ALLOWED_HOSTS = []

Line 

Line Line 

Line 

Line Line 

Line 

Line Line # Application definition

Line 

Line Line 

Line 

Line Line INSTALLED_APPS = [

Line 

Line Line     'django.contrib.admin',

Line 

Line Line     'django.contrib.auth',

Line 

Line Line     'django.contrib.contenttypes',

Line 

Line Line     'django.contrib.sessions',

Line 

Line Line     'django.contrib.messages',

Line 

Line Line     'django.contrib.staticfiles',

Line 

Line Line ]

Line 

Line Line 

Line 

Line Line MIDDLEWARE = [

Line 

Line Line     'django.middleware.security.SecurityMiddleware',

Line 

Line Line     'django.contrib.sessions.middleware.SessionMiddleware',

Line 

Line Line     'django.middleware.common.CommonMiddleware',

Line 

Line Line     'django.middleware.csrf.CsrfViewMiddleware',

Line 

Line Line     'django.contrib.auth.middleware.AuthenticationMiddleware',

Line 

Line Line     'django.contrib.messages.middleware.MessageMiddleware',

Line 

Line Line     'django.middleware.clickjacking.XFrameOptionsMiddleware',

Line 

Line Line ]

Line 

Line Line 

Line 

Line Line ROOT_URLCONF = 'valeria_crowdbotics_5.urls'

Line 

Line Line 

Line 

Line Line TEMPLATES = [

Line 

Line Line     {

Line 

Line Line         'BACKEND': 'django.template.backends.django.DjangoTemplates',

Line 

Line Line         'DIRS': [],

Line 

Line Line         'APP_DIRS': True,

Line 

Line Line         'OPTIONS': {

Line 

Line Line             'context_processors': [

Line 

Line Line                 'django.template.context_processors.debug',

Line 

Line Line                 'django.template.context_processors.request',

Line 

Line Line                 'django.contrib.auth.context_processors.auth',

Line 

Line Line                 'django.contrib.messages.context_processors.messages',

Line 

Line Line             ],

Line 

Line Line         },

Line 

Line Line     },

Line 

Line Line ]

Line 

Line Line 

Line 

Line Line WSGI_APPLICATION = 'valeria_crowdbotics_5.wsgi.application'

Line 

Line Line 

Line 

Line Line 

Line 

Line Line # Database

Line 

Line Line # https://docs.djangoproject.com/en/1.11/ref/settings/#databases

Line 

Line Line 

Line 

Line Line DATABASES = {

Line 

Line Line     'default': {

Line 

Line Line         'ENGINE': 'django.db.backends.sqlite3',

Line 

Line Line         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

Line 

Line Line     }

Line 

Line Line }

Line 

Line Line 

Line 

Line Line 

Line 

Line Line # Password validation

Line 

Line Line # https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

Line 

Line Line 

Line 

Line Line AUTH_PASSWORD_VALIDATORS = [

Line 

Line Line     {

Line 

Line Line         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',

Line 

Line Line     },

Line 

Line Line     {

Line 

Line Line         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',

Line 

Line Line     },

Line 

Line Line     {

Line 

Line Line         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',

Line 

Line Line     },

Line 

Line Line     {

Line 

Line Line         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',

Line 

Line Line     },

Line 

Line Line ]

Line 

Line Line 

Line 

Line Line 

Line 

Line Line # Internationalization

Line 

Line Line # https://docs.djangoproject.com/en/1.11/topics/i18n/

Line 

Line Line 

Line 

Line Line LANGUAGE_CODE = 'en-us'

Line 

Line Line 

Line 

Line Line TIME_ZONE = 'UTC'

Line 

Line Line 

Line 

Line Line USE_I18N = True

Line 

Line Line 

Line 

Line Line USE_L10N = True

Line 

Line Line 

Line 

Line Line USE_TZ = True

Line 

Line Line 

Line 

Line Line 

Line 

Line Line # Static files (CSS, JavaScript, Images)

Line 

Line Line # https://docs.djangoproject.com/en/1.11/howto/static-files/

Line 

Line Line 

Line 

Line Line STATIC_URL = '/static/'

Line 

Line Line 

Line 

Line Line import environ

Line 

Line Line env = environ.Env()

Line 

Line Line ALLOWED_HOSTS = ['*']

Line 

Line Line MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

Line 

Line Line 

Line 

Line Line DATABASES = {

Line 

Line Line     'default': env.db()

Line 

Line Line }

Line 

Line Line 

Line 

Line Line STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

Line 

Line Line STATICFILES_DIRS = [

Line 

Line Line     os.path.join(BASE_DIR, 'static')

Line 

Line Line ]

Line 

Line Line STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

Line 

