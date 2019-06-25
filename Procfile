release: python manage.py makemigrations && python manage.py migrate
web: gunicorn api.wsgi --log-file -
