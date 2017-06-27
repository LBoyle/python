from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from config import DevelopmentConfig

import os

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

class Example(db.Model):
    __tabename__ = 'example'
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Unicode)

    def __init__(self, id, data):
        self.id = id
        self.data = data

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Homepage'})

@app.route('/examples', methods=['GET'])
def examplesIndex():
    return jsonify({'examples': [{'id': example.id, 'data': example.data} for example in Example.query.all()]})

if __name__ == '__main__':
    # manager.run()
    app.run(debug=True, port=8080)
