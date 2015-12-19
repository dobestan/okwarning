web: gunicorn okwarning.wsgi -c etc/config/gunicorn.py
worker: celery --workdir=okwarning/ --app=okwarning.celery:app worker
beat: celery --workdir=okwarning/ --app=okwarning.celery:app beat
flower: celery --workdir=okwarning/ --app=okwarning.celery:app flower
