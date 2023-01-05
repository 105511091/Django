"""
Django settings for mydjango project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-@-5)h_y$prvno@=2qld_7y+af(96k8h+86v!q&^*i^(af(-tla"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #若正式上線時，請改為False

ALLOWED_HOSTS = ['*']#允許所有主機都可以進入
#['192.168.10.1','203.110.123.10']允許這二個IP連入


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'news',
    'product',
    'abouts',
    'message',
    'performance',
    'cart',
    'member',
    'photos',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mydjango.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR,'templates').replace('\\','/')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mydjango.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "mydjango",
        "USER":"myuser",
        "PASSWORD":"lcclcc",
        "HOST":"localhost",
        "PORT":'3306'
        #"OPTIONS":{
            #"init_command":"SETsql_mode='STRICT_TRANS_TABLES'",
            #}
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "zh-Hant" #設定後臺介面為繁體中文

TIME_ZONE = "Asia/Taipei"

USE_I18N = True

USE_TZ = False #不使用當地時間，使用TIME_ZONE 時區


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT=os.path.join(BASE_DIR,'static')#串聯專案資料夾

STATICFILES_DIRS=(
    
    ('images',os.path.join(STATIC_ROOT,'images').replace('\\','/')),
    ('css',os.path.join(STATIC_ROOT,'css').replace('\\','/')),
    ('js',os.path.join(STATIC_ROOT,'js').replace('\\','/')),
    
    
    )
#設定瀏覽器關閉時，SESSION就關掉 True 是關掉 預設是False =>不關
#SESSION_EXPIRE_AT_BROWSER_CLOSE = True

#設定多媒體資料夾

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')




# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"