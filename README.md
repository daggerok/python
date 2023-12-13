# python [![CI](https://github.com/daggerok/python/actions/workflows/ci.yml/badge.svg)](https://github.com/daggerok/python/actions/workflows/ci.yml)
Python

## Boris

dev:
* pytest ✔
* pylint ✔
* behave ✔
* pyenv ✔
* pip3 ✔
* pep8 ✔
* pycodestyle ✔
* makefile

web/crud api:
* flask
* flask-api
* flask_restful
* flask-rest-jsonapi-next
* Flask-Injector
* sqlalchemy
* pydantic
* data-mapper
* fastapi
* flask vs fastapi (when use what and why / right tool for right job

misc:
* pandas
* boto3

aws:
* jobs: Glue pyshell + GLue Triggers + Cloudformation

## Serdak

python:
* pandas
* sql alchemy

angular
azure

## getting started

```bash
python -m venv .venv
source .venv/bin/activate
pip install ...
# ...
deactivate
```

## requirements file

Generate `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

Install packages specified in `requirements.txt` and in `requirements-dev.txt` files:

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

## cleanup

```bash
for i in `find . -name '*.pytest_cache' -type d` ; do rm -rfv $i ; done
```

## rtfm
* https://behave.readthedocs.io/en/latest/
* https://docs.pytest.org/en/7.4.x/getting-started.html
* https://learnpython.com/blog/python-requirements-file/
* https://realpython.com/intro-to-pyenv/
