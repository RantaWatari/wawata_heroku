web: gunicorn gettingstarted.wsgi
web: flask init-db
web: gunicorn flask_file:'create_app()' --log-file=-