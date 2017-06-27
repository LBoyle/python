# Migrations / My first API design pattern

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

- Create virtualenv in the project root, I use ```virtualenv -p python3 venv``` and activate with ```. venv/bin/activate```.

- Install Flask dependancies with pip.

- Create the DB, ensure PostgreSQL is running with ```python db/db.py db init```, ```python db/db.py db migrate``` then ```python db/db.py db upgrade``` in that order.

- Seed data with ```python db/seeds.py```.

- Start the API server with ```python app.py```.


***

Using flask_migrate. Also trying a join-table.

An example of a query I can use with this setup.
```
Channel.query.first().subscribers.first().name
```

## Oops

This exercise has evolved beyond its initial scope, I'm pretty much making it up as I go.

I've based this so far on my knowledge of other MVC frameworks, specifically Express.js and Rails.
