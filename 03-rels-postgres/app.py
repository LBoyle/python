from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(20))
    pets = db.relationship('Pet', backref='owner', lazy='dynamic')
# backref is a virtual column
# lazy allows querying as follows
# Person.query.all()[0].pets.all()
# etc. 

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))

# after writing this I used the idle to create the tables
# db.create_all()
# db.session.commit()
