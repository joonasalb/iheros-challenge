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
cp .env.development .env
docker build -t iheros-backend .
## Deploy
docker run --env-file=.env.development --network=host -d iheros-backend
```

Runs the server in the development mode.<br />
Open [http://localhost:8000](http://localhost:8000)

## Database

The default database in production is postgres and the default when testing is 
sqlite. To use the postgres database you must configure the `.env` file 
(`.env.production` can be used as a template)

If you don't have an postgres instance configured you can use the 
`docker/postgres.yml` file. To install it you need docker-compose:

```shell
docker-compose -f docker/postgres.yml up -d
```

## Run unit tests
Run application unit test
```shell
python manage.py test
```

### Run unit test
```shell
python manage.py test
```

### Postman collection
```shell
./ZRP Challange.postman_collection.json
```

### Postman Environment
```shell
./ZRP Challange.postman_environment.json
```
