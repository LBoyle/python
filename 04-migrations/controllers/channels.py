from flask import jsonify

from db import Channel

def channelsIndex():
    return jsonify({'channels': [{'id': c.id, 'name': c.name, 'subscribers': [{'id': u.id, 'name': u.name} for u in c.subscribers]} for c in Channel.query.all()]})

def channelsShow(id):
    return jsonify({'channel': [{'id': c.id, 'name': c.name, 'subscribers': [{'id': u.id, 'name': u.name} for u in c.subscribers]} for c in Channel.query.filter_by(id=id)][0]})
