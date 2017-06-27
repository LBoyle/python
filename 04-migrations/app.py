from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
BASE_URL = 'http://localhost:8080'
from controllers import base, users, channels

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

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
@app.route('/channels/<int:id>', methods=['GET'])
def channelsShow(id):
    return channels.show(id)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
