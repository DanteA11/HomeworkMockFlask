FROM python:3.12

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY application/ /app
COPY uwsgi.ini /etc/uwsgi/uwsgi.ini

WORKDIR /app

CMD ["/usr/local/bin/uwsgi", "--ini", "/etc/uwsgi/uwsgi.ini"]
