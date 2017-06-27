from flask import jsonify, request
from app import BASE_URL, db
from serializers import user

from db import manage
User = manage.User

def index():
    return jsonify({
        '_home': BASE_URL,
        'users': [user.userSerializer(u) for u in User.query.all()]
    })

def show(id):
    return jsonify({
        '_home': BASE_URL,
        'user': [user.userSerializer(u) for u in User.query.filter_by(id=id)][0]
    })

def new():
    newUser = User(request.json['id'], request.json['name'])
    db.session.add(newUser)
    db.session.commit()
    return index()
