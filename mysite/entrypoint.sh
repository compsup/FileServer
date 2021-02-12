set -e

python manage.py migrate --noinput
python manage.py runserver 0.0.0.0:8000 --settings=mysite.settings.production --insecure