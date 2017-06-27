from flask import jsonify
from app import BASE_URL
from serializers import channel

from db import db
Channel = db.Channel

def index():
    return jsonify({'_home': BASE_URL, 'channels': [channel.channelSerializer(c) for c in Channel.query.all()]})

def show(id):
    return jsonify({'_home': BASE_URL, 'channel': [channel.channelSerializer(c) for c in Channel.query.filter_by(id=id)][0]})
