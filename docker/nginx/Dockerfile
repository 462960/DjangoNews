FROM nginx:latest

RUN mkdir -p /app/static
WORKDIR /app
ADD project/news_project/static /app/static
COPY docker/nginx/config/django_news.conf /etc/nginx/conf.d/default.conf