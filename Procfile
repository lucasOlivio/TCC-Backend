release: python manage.py makemigrations invest_back_end && python manage.py migrate
web: gunicorn api.wsgi --log-file -
