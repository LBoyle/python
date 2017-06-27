# Migrations
#### / My first API design pattern

Ongoing

## Dependancies

- Python 3.6 and virtualenv
- Flask
- PostgreSQL
- SQLAlchemy
- psycopg2
- flask-migrate

#### Dev Installation
<small>Linux or OSX</small>

- Clone the repo

- Make a config.py file, see below

- Create virtualenv in the project root, I use ```virtualenv -p python3 venv``` and activate with ```. venv/bin/activate```.

- Install Flask dependancies with pip.

- Ensure PostgreSQL is running and create the DB with ```python db/db.py db init```, ```python db/db.py db migrate``` then ```python db/db.py db upgrade``` in that order.

- Seed data with ```python db/seeds.py```.

- Start the API server with ```python app.py```.

### Config

Make a file called config.py in the project root, it should contain something like as follows.

```

class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'do-i-really-need-this'
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/dbname'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_URL = 'http://localhost:8080'

class DevConfig(Config):
    DEBUG = True
    DEVELOPMENT = True

...

```


## Oops

This exercise has exceeded its initial scope, I'm pretty much making it up as I go because I'm having fun.

I've based this so far on my knowledge of other MVC frameworks, specifically Express.js and Rails.
