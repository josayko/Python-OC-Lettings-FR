# Epic Events CRM

## Installation

### Prerequisites

- `python >= 3.9`, `pip`, `venv`
- you can manage different `python` versions with **[pyenv](https://github.com/pyenv/pyenv)**
- `docker`

### Get started

#### Local development environment

```bash
$ python -m venv env
```

```bash
$ source env/bin/activate
```

```bash
$  pip install -r requirements.txt
```

#### Environement variables

- Generate a `.env.TEMPLATE` file

```
$ python setup_env.py
```

- Rename the file to `.env` and configure the variables

```bash
# .env
DJANGO_SECRET_KEY=
DEBUG=
SENTRY_DSN=
HEROKU_API_KEY=
HEROKU_APP_NAME=
```

#### Setting up database

- Migrate database

```bash
$ python manage.py migrate
```

- Populate some data in the database

```bash
$ make fixture
# alternatively:
# $ python manage.py loaddata users addresses lettings profiles
```

## Running the app

```bash
$ python manage.py runserver
```

> The API is running on http://localhost:8000/ by default

> You can access admin dashboard on http://localhost:8000/admin, if data has been loaded previously from `fixture/`, there is a default admin user `admin` with password `Abc1234!`

- Execute linting

```bash
$ flake8
```

- Execute unit tests

```bash
$ pytest
```

## Dockerization

#### Build an run a docker image locally

- An image of the app will be build from `Dockerfile`

```bash
$ docker build -t [IMAGE_NAME] .
```

- Start a container from the image

```bash
$ docker run --rm -p 8000:8000 --env-file .env [IMAGE_NAME]
```

#### Pull the image from Docker Hub

- Sign in to Docker Hub

```bash
$ docker pull
```

## Author

- Jonny Saykosy <josayko@pm.me>

## License & copyright

© Jonny Saykosy

Licensed under the [MIT License](LICENSE).
