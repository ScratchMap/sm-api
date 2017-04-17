# Scratch-map API

## Manage dependencies

### Setup dependencies
Run next commands in bash:

> `$ virtualenv -p python3 venv`

> `$ source venv/bin/activate`

> `$ sudo pip install -r requirements.txt`

### Freeze dependencies
After install new dependence please use:
> `$ pip freeze > requirements.txt`

### Deactivate virtual environment
Run `$ deactivate` in bash


## Run project
### to run project locally
use `$ ./manage.py runserver`

### to run project with production config
use `$ ./manage.py -c config/production.py runserver`


## Linter
In project installed linter [flake8](http://flake8.pycqa.org/en/latest/index.html)
