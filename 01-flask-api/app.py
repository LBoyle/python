from flask import Flask, jsonify, request
app = Flask(__name__)

languages = [{'name': 'JavaScript'}, {'name': 'Python'}, {'name': 'Ruby'}]

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Homepage'})

@app.route('/langs', methods=['GET'])
def langsIndex():
    return jsonify({'languages': languages})

@app.route('/langs/<string:name>', methods=['GET'])
def langsOne(name):
    return jsonify({'language': [language for language in languages if language['name'] == name][0]})

@app.route('/langs', methods=['POST'])
def langsCreate():
    lang = {'name': request.json['name']}
    languages.append(lang)
    return jsonify({'languages': languages})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
