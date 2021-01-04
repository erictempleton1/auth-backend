#!/bin/bash

django-admin startproject auth_project
cd auth_project
django-admin startapp auth_demo
# Add auth_demo to auto_project/settings.py
# pip install psycopg2 as needed
# Update the default database in auth_project/settings.py
# 'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'postgres',
#        'USER': 'postgres',
#        'PASSWORD': 'postgres',
#        'HOST': '127.0.0.1',
#        'PORT': '5432',
# }
python manage.py makemigrations
python manage.py migrate
