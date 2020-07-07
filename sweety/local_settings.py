import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sweety',
        'USER': 'postgres',
        'PASSWORD': 'sweety123suhane',
        'HOST' : 'localhost',
        'PORT'  :   '5432',
    }
}
