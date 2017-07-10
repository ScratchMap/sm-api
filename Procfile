web2: python3 manage.py -c config/production.py runserver
web: gunicorn manager:app -c config/production.py
db_upgrade: python3 manage.py -c config/production.py db upgrade