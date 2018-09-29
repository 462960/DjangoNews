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