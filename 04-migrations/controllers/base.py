from flask import jsonify
from app import BASE_URL

def home():
    return jsonify({'message': 'Welcome to the site', 'links': [{'channels': BASE_URL+'/channels'},{'users': BASE_URL+'/users'}]})
