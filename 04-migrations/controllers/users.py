from flask import jsonify
from app import BASE_URL
# BASE_URL+

from db import User

def usersIndex():
    return jsonify({'_home': BASE_URL, 'users': [{'id': u.id,'name': u.name, 'link': BASE_URL+'/users/'+str(u.id), 'subscriptions': [{'id': c.id, 'name': c.name, 'link': BASE_URL+'/channels/'+str(c.id)} for c in u.subscriptions]} for u in User.query.all()]})

def usersShow(id):
    return jsonify({'_home': BASE_URL, 'user': [{'id': u.id, 'name': u.name, 'subscriptions': [{'id': c.id, 'name': c.name, 'link': BASE_URL+'/channels/'+str(c.id)} for c in u.subscriptions]} for u in User.query.filter_by(id=id)][0]})
