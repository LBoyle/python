from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from db import User, Channel

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the site'})

@app.route('/users', methods=['GET'])
def usersIndex():
    return jsonify({'users': [{'id': user.id,'name': user.name, 'subscriptions': [{'': channel.id, 'name': channel.name} for channel in user.subscriptions]} for user in User.query.all()]})

@app.route('/channels', methods=['GET'])
def channelsIndex():
    return jsonify({'channels': [{'id': channel.id, 'name': channel.name, 'subscribers': [{'id': user.id, 'name': user.name} for user in channel.subscribers]} for channel in Channel.query.all()]})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
