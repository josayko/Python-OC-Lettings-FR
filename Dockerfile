FROM python:3.10.4

WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /app
ARG DJANGO_SECRET_KEY
ENV DJANGO_SECRET_KEY ${DJANGO_SECRET_KEY}
ARG SENTRY_DSN
ENV SENTRY_DSN ${SENTRY_DSN}
RUN python manage.py collectstatic --noinput
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]