FROM python:3.6

ENV DJANGO_SETTINGS_MODULE=news_project.settings.production
ARG requirements=requirements/production.txt

RUN mkdir /app \
&& echo "ARG: requirements ------------------ ${requirements}" \
&& echo "ENV: DJANGO_SETTINGS_MODULE -------- ${DJANGO_SETTINGS_MODULE}"

WORKDIR /app

ADD $requirements /app/requirements.txt
RUN pip install -r requirements.txt
ADD project /app