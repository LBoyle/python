from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.DevConfig')
BASE_URL = app.config['BASE_URL']
db = SQLAlchemy(app)

from controllers import base, users, channels

@app.route('/', methods=['GET'])
def home():
    return base.home()

@app.route('/users', methods=['GET'])
def usersIndex():
    return users.index()
@app.route('/users', methods=['POST'])
def usersNew():
    return users.new()
@app.route('/users/<int:id>', methods=['GET'])
def usersShow(id):
    return users.show(id)
@app.route('/users/<int:id>', methods=['DELETE'])
def usersDelete(id):
    return users.delete(id)

@app.route('/channels', methods=['GET'])
def channelsIndex():
    return channels.index()
@app.route('/channels', methods=['POST'])
def channelsNew():
    return channels.new(db)
@app.route('/channels/<int:id>', methods=['GET'])
def channelsShow(id):
    return channels.show(id)
@app.route('/channels/<int:id>', methods=['DELETE'])
def channelsDelete(id):
    return channels.delete(id, db)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
