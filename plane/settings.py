# from pathlib import Path
#
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
#
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-0%4(pjg18b11-(8n2vswibl1neq-6m+7b203v#00r$1^0c75lg"
#
# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# ALLOWED_HOSTS = []
#
# # Application definition
#
# INSTALLED_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
#     # local
#     "accounts.apps.AccountsConfig",
#     "airlines.apps.AirlinesConfig",
#     "passangers.apps.PassangersConfig",
#     "hotels.apps.HotelsConfig",
#     "core.apps.CoreConfig",
#     # third
#     "widget_tweaks",
#     "django_extensions",
#     "braces",
#     "azbankgateways",
# ]
#
# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]
#
# ROOT_URLCONF = "plane.urls"
#
# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": [BASE_DIR / "templates"],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#
#                 # local
#                 'core.context_processors.access_setting',
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = "plane.wsgi.application"
#
# # Database
# # https://docs.djangoproject.com/en/4.0/ref/settings/#databases
#
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
#
# # Password validation
# # https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]
#
# # Internationalization
# # https://docs.djangoproject.com/en/4.0/topics/i18n/
#
#
# TIME_ZONE = "UTC"
#
# USE_I18N = True
#
# USE_TZ = True
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/4.0/howto/static-files/
# STATIC_URL = "/static/"
# STATICFILES_DIRS = [
#     BASE_DIR / "assets",
# ]
#
# STATIC_ROOT = BASE_DIR / "static_cdn" / "static"
#
# MEDIA_URL = "/media/"
#
# MEDIA_ROOT = BASE_DIR / "static_cdn" / "media"
#
# # Default primary key field type
# # https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
#
# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# AUTH_USER_MODEL = "accounts.User"
#
# AZ_IRANIAN_BANK_GATEWAYS = {
#     "GATEWAYS": {
#         "BMI": {
#             "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
#             "TERMINAL_CODE": "<YOUR TERMINAL CODE>",
#             "SECRET_KEY": "<YOUR SECRET CODE>",
#         },
#         "SEP": {
#             "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
#             "TERMINAL_CODE": "<YOUR TERMINAL CODE>",
#         },
#         "ZARINPAL": {
#             "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
#         },
#         "IDPAY": {
#             "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
#             "METHOD": "POST",  # GET or POST
#             "X_SANDBOX": 0,  # 0 disable, 1 active
#         },
#         "ZIBAL": {
#             "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
#         },
#         "BAHAMTA": {
#             "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
#         },
#         "MELLAT": {
#             "TERMINAL_CODE": "<YOUR TERMINAL CODE>",
#             "USERNAME": "<YOUR USERNAME>",
#             "PASSWORD": "<YOUR PASSWORD>",
#         },
#     },
#     "IS_SAMPLE_FORM_ENABLE": True,  # اختیاری و پیش فرض غیر فعال است
#     "DEFAULT": "BMI",
#     "CURRENCY": "IRR",  # اختیاری
#     "TRACKING_CODE_QUERY_PARAM": "tc",  # اختیاری
#     "TRACKING_CODE_LENGTH": 16,  # اختیاری
#     "SETTING_VALUE_READER_CLASS": "azbankgateways.readers.DefaultReader",  # اختیاری
#     "BANK_PRIORITIES": [
#         "BMI",
#         "SEP",
#         # and so on ...
#     ],  # اختیاری
# }
#
# LANGUAGE_CODE = "fa-ir"
#
#
#
#
#















import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-0%4(pjg18b11-(8n2vswibl1neq-6m+7b203v#00r$1^0c75lg"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['booking.darkube.app' , 'www.booking.darkube.app']

# Application definition

INSTALLED_APPS = [
    'adminlte3',
    'adminlte3_theme',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # local
    "accounts.apps.AccountsConfig",
    "airlines.apps.AirlinesConfig",
    "passangers.apps.PassangersConfig",
    "hotels.apps.HotelsConfig",
    "core.apps.CoreConfig",
    # third
    "widget_tweaks",
    "django_extensions",
    "braces",
    "azbankgateways",
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

ROOT_URLCONF = "plane.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",

                # local
                'core.context_processors.access_setting',
            ],
        },
    },
]

WSGI_APPLICATION = "plane.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/


TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "assets",
]

STATIC_ROOT = BASE_DIR / "static_cdn" / "static"

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "static_cdn" / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "accounts.User"

AZ_IRANIAN_BANK_GATEWAYS = {
    "GATEWAYS": {
        "BMI": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
            "TERMINAL_CODE": "<YOUR TERMINAL CODE>",
            "SECRET_KEY": "<YOUR SECRET CODE>",
        },
        "SEP": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
            "TERMINAL_CODE": "<YOUR TERMINAL CODE>",
        },
        "ZARINPAL": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
        },
        "IDPAY": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
            "METHOD": "POST",  # GET or POST
            "X_SANDBOX": 0,  # 0 disable, 1 active
        },
        "ZIBAL": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
        },
        "BAHAMTA": {
            "MERCHANT_CODE": "<YOUR MERCHANT CODE>",
        },
        "MELLAT": {
            "TERMINAL_CODE": "<YOUR TERMINAL CODE>",
            "USERNAME": "<YOUR USERNAME>",
            "PASSWORD": "<YOUR PASSWORD>",
        },
    },
    "IS_SAMPLE_FORM_ENABLE": True,  # اختیاری و پیش فرض غیر فعال است
    "DEFAULT": "BMI",
    "CURRENCY": "IRR",  # اختیاری
    "TRACKING_CODE_QUERY_PARAM": "tc",  # اختیاری
    "TRACKING_CODE_LENGTH": 16,  # اختیاری
    "SETTING_VALUE_READER_CLASS": "azbankgateways.readers.DefaultReader",  # اختیاری
    "BANK_PRIORITIES": [
        "BMI",
        "SEP",
        # and so on ...
    ],  # اختیاری
}


