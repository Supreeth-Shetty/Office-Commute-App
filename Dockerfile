FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --bind=0.0.0.0:$PORT --workers=4 office_commute_app_main.wsgi