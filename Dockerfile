FROM python:3.12.0-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV APP /var/www/app

WORKDIR $APP

# Install system requirements
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt install -y gcc python3-dev build-essential g++ procps --fix-missing libpq-dev \
    && pip install --upgrade pip \
    && rm -rf /var/lib/apt/lists/* \
    && chown -R www-data:www-data /var/www

ADD ./backend/requirements.txt $APP

RUN pip install --disable-pip-version-check --exists-action w -r requirements.txt

ADD ./backend/ $APP

USER www-data

EXPOSE 5000

CMD ["bash", "-c", "/var/www/app/scripts/start_server.sh"]
