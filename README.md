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
## Coverage

```
coverage run --source='news' manage.py test
coverage html
# or
coverage report
```