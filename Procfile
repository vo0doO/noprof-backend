release: yes "yes" | python manage.py migrate
web: uwsgi --http-socket=:$PORT --master --workers=2 --threads=8 --die-on-term --wsgi-file=portfolio/wsgi.py  --static-map /media/=/app/portfolio/media/ --offload-threads 1
