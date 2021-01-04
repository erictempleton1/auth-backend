Start the project and create the app
`django-admin startproject <project-name>`
`cd <project-name>`
`django-admin startapp <app-name>`

If using postgres, install psycopg2
`pip install psycopg2`

Add the <app-name> from above to the `INSTALLED_APPS` list in `<project-name>/settings.py`

Update the database settings in `<project-name>/settings.py`
```python
'default': {
  'ENGINE': 'django.db.backends.postgresql',
  'NAME': '<database-name>',
  'USER': '<database-user>',
  'PASSWORD': '<user-password>',
  'HOST': '127.0.0.1',
  'PORT': '5432',
}
``` 

Make and apply migrations
`python manage.py makemigrations`
`python manage.py migrate`

Run the server
`python manage.py runserver`
