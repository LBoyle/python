from flask import jsonify

from db import User

def usersIndex():
    return jsonify({'users': [{'id': u.id,'name': u.name, 'subscriptions': [{'': c.id, 'name': c.name} for c in u.subscriptions]} for u in User.query.all()]})

def usersShow(id):
    return jsonify({'user': [{'id': u.id, 'name': u.name, 'subscriptions': [{'id': c.id, 'name': c.name} for c in u.subscriptions]} for u in User.query.filter_by(id=id)][0]})
