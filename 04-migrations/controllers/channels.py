from flask import jsonify, request
from app import BASE_URL
from serializers import channel

from db import manage
Channel = manage.Channel

def index():
    return jsonify({
        '_home': BASE_URL,
        'channels': [channel.channelSerializer(c) for c in Channel.query.all()]
    })

def show(id):
    return jsonify({
        '_home': BASE_URL,
        'channel': [channel.channelSerializer(c) for c in Channel.query.filter_by(id=id)][0]
    })

def new(db):
    newChannel = Channel(request.json['id'], request.json['name'])
    db.session.add(newChannel)
    db.session.commit()
    return index()

def delete(id, db):
    toDelete = Channel.query.filter_by(id=id).first()
    db.session.delete(toDelete)
    db.session.commit()
    return index()
