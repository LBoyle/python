from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db import User, Channel

app = Flask(__name__)
app.config.from_pyfile('../config.cfg')
db = SQLAlchemy(app)

u1 = User(id=1, name='Louis')
u2 = User(id=2, name='John')

c1 = Channel(id=1, name='LTT')
c2 = Channel(id=2, name='Epic Meal Time')

c1.subscribers.append(u1)
c1.subscribers.append(u2)
c2.subscribers.append(u2)

db.session.add(u1)
db.session.add(u2)
db.session.add(c1)
db.session.add(c2)
db.session.commit()

db.session.close()
