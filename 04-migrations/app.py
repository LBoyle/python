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
@app.route('/users/<int:id>', methods=['GET'])
def usersShow(id):
    return users.show(id)

@app.route('/channels', methods=['GET'])
def channelsIndex():
    return channels.index()
@app.route('/channels', methods=['POST'])
def channelsNew():
    return channels.new()
@app.route('/channels/<int:id>', methods=['GET'])
def channelsShow(id):
    return channels.show(id)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
