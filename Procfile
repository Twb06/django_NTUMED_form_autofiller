web: gunicorn NTUMEDformautofiller.wsgi --timeout 30 --log-file -
worker: celery -A NTUMEDformautofiller worker -l info -c 4