from pathlib import Path
import cloudinary
import os

envget = lambda var : os.environ.get(var)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = envget('SECRET_KEY') # add to heroku venv vars

DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # My apps:
    'VolgaREST.root',
    # 3rd frameworks apps:
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'cloudinary'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 3rd frameworks middlewares:
    'corsheaders.middleware.CorsMiddleware',
    # My middlewares:
    'VolgaREST.endpoints.custom.IdentifyUserMiddleware'
]

ROOT_URLCONF = 'VolgaREST.urls'

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

WSGI_APPLICATION = 'VolgaREST.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

# My config:

AUTH_USER_MODEL = 'root.UserModel'

CORS_ALLOW_ALL_ORIGINS = True

ALLOWED_HOSTS = ['https://volga-644ec.web.app/']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
}

cloudinary.config(
    cloud_name='volga-cloud',
    api_key=envget('CLOUDINARY_API_KEY'),
    api_secret=envget('CLOUDINARY_API_SECRET')
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = envget('EMAIL_PASSWORD')
EMAIL_HOST_USER = 'thevolgaproject2021@gmail.com'
