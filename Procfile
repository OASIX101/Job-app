web: gunicorn -b "0.0.0.0:$PORT" -w 3 job_app.wsgi
release: python manage.py migrate