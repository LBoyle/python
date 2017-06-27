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

- Create virtualenv in the project root, I use ```virtualenv -p python3 venv``` and activate with ```. venv/bin/activate```.

- Install Flask dependancies with pip.

- Ensure PostgreSQL is running and create the DB with ```python db/db.py db init```, ```python db/db.py db migrate``` then ```python db/db.py db upgrade``` in that order.

- Seed data with ```python db/seeds.py```.

- Start the API server with ```python app.py```.


## Oops

This exercise has exceeded its initial scope, I'm pretty much making it up as I go because I'm having fun.

I've based this so far on my knowledge of other MVC frameworks, specifically Express.js and Rails.
