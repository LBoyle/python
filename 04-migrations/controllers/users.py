from flask import jsonify
from app import BASE_URL
from serializers import user

from db import db
User = db.User

def index():
    return jsonify({'_home': BASE_URL, 'users': [user.userSerializer(u) for u in User.query.all()]})

def show(id):
    return jsonify({'_home': BASE_URL, 'user': [user.userSerializer(u) for u in User.query.filter_by(id=id)][0]})
