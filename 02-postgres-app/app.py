from flask import Flask, jsonify, request
from flask_sqlalchemy import
app = Flask(__name__)

languages = [{'name': 'JavaScript'}, {'name': 'Python'}, {'name': 'Ruby'}]

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Homepage'})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
