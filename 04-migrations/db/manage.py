from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_pyfile('dbconf.cfg')
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
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(20))
    def __init__(self, id, name):
        self.id = id
        self.name = name

if __name__ == '__main__':
    manager.run()
