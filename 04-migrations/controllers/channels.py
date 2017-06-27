from flask import jsonify
from app import BASE_URL

from db import Channel

def channelsIndex():
    return jsonify({'_home': BASE_URL, 'channels': [{'id': c.id, 'name': c.name, 'link': BASE_URL+'/channels/'+str(c.id), 'subscribers': [{'id': u.id, 'name': u.name, 'link': BASE_URL+'/users/'+str(u.id)} for u in c.subscribers]} for c in Channel.query.all()]})

def channelsShow(id):
    return jsonify({'_home': BASE_URL, 'channel': [{'id': c.id, 'name': c.name, 'subscribers': [{'id': u.id, 'name': u.name, 'link': BASE_URL+'/users/'+str(u.id)} for u in c.subscribers]} for c in Channel.query.filter_by(id=id)][0]})
