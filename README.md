# DjangoNews

## Install virtualenv

```
sudo apt-get install python3-pip
sudo pip3 install virtualenv 

virtualenv -p $(which python3) venv
```

## Activate virtualenv

```
source venv/bin/activate
```
## Backend test

### Coverage

```
coverage run --source='news' manage.py test
coverage html
# or
coverage report
```

## Frontend test

```
npm run e2e
```

## Docker

### Develop
```
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
```

### Deploy
```
docker-machine create --driver digitalocean --digitalocean-access-token $DIGITALOCEAN_ACCESS_TOKEN django_news
eval $(docker-machine env django-news)
docker-compose -f docker-compose.yml -f docker-compose.prod.yml build
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

## Auth

### Register
```
curl --request POST \
--url http://localhost:8000/api/auth/register/ \
--header 'content-type: application/json' \
--data '{
  "username": "user",
  "password": "qwerty"
}'
```

### Login
```
curl --request POST \
  --url http://localhost:8000/api/auth/login/ \
  --header 'content-type: application/json' \
  --data '{
    "username": "user",
    "password": "qwerty"
}'
```

### Current user
```
curl --request GET \
  --url http://localhost:8000/api/auth/user/ \
  --header 'authorization: Token YOUR_API_TOKEN_HERE' \
  --header 'content-type: application/json' \
```