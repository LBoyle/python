from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

subs = db.Table('subs',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('channel_id', db.Integer, db.ForeignKey('channel.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(20))
    subscriptions = db.relationship('Channel', secondary=subs, backref=db.backref('subscribers', lazy='dynamic'))

class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(20))

if __name__ == '__main__':
    manager.run()
