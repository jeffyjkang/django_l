django-admin startproject wisdompets

manage.py runs commands
__init__.py tells python that the folder contains python code
wsgi.py and asgi.py provides hooks for webservers like apache or nginx when django is running live
settings.py configs django project
urls.py routes web requests based on url
python manage.py runserver

apps: settings specific to app
models: provides data layer that django uses to construct db schema and queries
admin: defines administrative interface for app hat allows us to see and edit the data
urls: url routing specific to app
views: defines logic and control flow for handling requests and defines the http res
tests: writing unit tests
migrations/: holds files which django uses to migrate db as we change db schema over time

python manage.py makemigrations ->
generates migration files for later use, uses current model fields and current db tables,
creates numbered files in appname/migrations/
python manage.py showmigrations
python manage.py migrate ->
runs all migrations in the project to the current state,
can also run only migrations in specific app to specific number:
  python manage.py migrate <appname> <number>
