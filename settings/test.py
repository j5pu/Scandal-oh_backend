"""Testing settings."""

from settings.common import *
from settings import common

common.TEST_MODE = True

# Usaremos sqlite3 como BD para testing
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': ':memory:',					  # Or path to database file if using sqlite3.
        'USER': '',					  # Not used with sqlite3.
        'PASSWORD': '',				  # Not used with sqlite3.
        'HOST': '',					  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',					  # Set to empty string for default. Not used with sqlite3.
    }
}

INSTALLED_APPS += (
    'selenium',
    'django_nose',
    # 'lettuce.django',
    'tests',
)


# LETTUCE
#########################################
# LETTUCE_APPS = (
#     'tests',
# )
# LETTUCE_AVOID_APPS = (
#     'another_app',
#     'foobar',
# )
# LETTUCE_SERVER_PORT = 7000
#########################################


# NOSE
#########################################
TEST_RUNNER = 'tests.runner.MyTestRunner'
# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '-s', # para activar stdout (salida a consola) durante los tests
    '--verbosity=2',
]

import os
os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = 'localhost:7000'
#########################################
