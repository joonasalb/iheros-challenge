# IHeros Back-End

## Local Environment

Requirements: Python3.7^

```shell
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Docker / Production Environment

```shell
cp .env.production .env
docker build -t iheros .
## Deploy
docker run --env-file=.env --network=host -d --name iheros iheros
```

## Database

The default database in production is postgres and the default when testing is 
sqlite. To use the postgres database you must configure the `.env` file 
(`.env.production` can be used as a template)

## Run unit tests
Run application unit test
```shell
    python manage.py test
```

### Run unit test
```shell
python manage.py test
```