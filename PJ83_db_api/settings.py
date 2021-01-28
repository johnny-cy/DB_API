"""
Django settings for PJ83_db_api project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

try:
    ENV = os.environ["ENV"]
except:
    raise NotImplementedError("Variable ENV not found, it needs to be defined from docker-compose.yml")
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '47&0sx6llt^3_owzv$(u=qy#@48hffvla#6%f*=ji3hs!h#yfj'

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
    # 'db_api',
    # 'rest_framework', # Django REST framework
    # 'db_api.apps.DbApiConfig',
    # 'corsheaders', #CORS
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware', #CORS
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware', #CORS
]

ROOT_URLCONF = 'PJ83_db_api.urls'
CORS_ORIGIN_ALLOW_ALL = True #CORS
CORS_ORIGIN_WHITELIST = ( #CORS
    'http://localhost:8081',
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                # 'django.template.context_processors.media', #
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PJ83_db_api.wsgi.application'


REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',

    ]
}




# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

if ENV == 'DEV':
    """
    No read-write seperated, both master and slave use same db.
    """
    DATABASES = {
        'default': { # default, master
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'DEV_PJ83BN',
            'USER': 'root',
            'PASSWORD': '1qaz@WSX',
            'HOST': '10.80.1.15',
            'PORT': '30010',
        },
        'slave': { # Read-Only
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'DEV_PJ83BN',
            'USER': 'root',
            'PASSWORD': '1qaz@WSX',
            'HOST': '10.80.1.15',
            'PORT': '30010',
        }
    }
elif ENV == 'UAT':
    """
    No read-write seperated, both master and slave use same db.
    """
    DATABASES = {
        'default': { # default, master
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'UAT_PJ83BN',
            'USER': 'root',
            'PASSWORD': '1qaz@WSX',
            'HOST': '10.80.1.15',
            'PORT': '30020',
        },
        'slave': { # Read-Only
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'UAT_PJ83BN',
            'USER': 'root',
            'PASSWORD': '1qaz@WSX',
            'HOST': '10.80.1.15',
            'PORT': '30020',
        }
    }
elif ENV == 'PROD':
    """
    No read-write seperated, both master and slave use same db.
    """
    DATABASES = {
        'default': { # default, master
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'PJ83BN',
            'USER': 'root',
            'PASSWORD': '1qaz@WSX',
            'HOST': '10.80.1.15',
            'PORT': '30030',
        },
        'slave': { # Read-Only
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'PJ83BN',
            'USER': 'root',
            'PASSWORD': '1qaz@WSX',
            'HOST': '10.80.1.15',
            'PORT': '30030',
        }
    }
elif ENV == 'ALIYUN':
    """
    read-write seperated (CQRS)
    """
    DATABASES = {
        'default': { # default, master
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'PJ83BN',
            'USER': 'root',
            'PASSWORD': 'qwer1234',
            'HOST': '172.28.0.10',
            'PORT': '3306',
        },
        'slave': { # Read-Only
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'PJ83BN',
            'USER': 'root',
            'PASSWORD': 'qwer1234',
            'HOST': '172.28.0.11',
            'PORT': '3306',
        }
    }
elif ENV == 'DEV2':
    """
    No read-write seperated, both master and slave use same db.
    """
    DATABASES = {
        'default': { # default, master
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'DEV_PJ83BN',
            'USER': 'root',
            'PASSWORD': '1qaz@WSX',
            'HOST': '10.10.0.150',
            'PORT': '30010',
        },
        'slave': { # Read-Only
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'DEV_PJ83BN',
            'USER': 'root',
            'PASSWORD': '1qaz@WSX',
            'HOST': '10.10.0.150',
            'PORT': '30010',
        }
    }


# DATABASES = {
#     'default': { # default, master
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'DEV_PJ83BN',
#         'USER': 'root',
#         'PASSWORD': 'qwer1234',
#         'HOST': '172.28.0.10',
#         'PORT': '3306',
#     },
#     'slave': { # Read-Only
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'DEV_PJ83BN',
#         'USER': 'root',
#         'PASSWORD': 'qwer1234',
#         'HOST': '172.28.0.11',
#         'PORT': '3306',
#     },
#     'test':{
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'testdb',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
# }


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

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/' # 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #

