from prplapi.settings.base
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'prplapi',
        'USER': 'prpl',
        'PASSWORD':  None,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}