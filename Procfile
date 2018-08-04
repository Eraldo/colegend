web: gunicorn config.wsgi:application
worker: celery worker --app=colegend.taskapp --loglevel=info
