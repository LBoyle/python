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
    return jsonify({'language': [lang for lang in languages if lang['name'] == name][0]})

@app.route('/langs', methods=['POST'])
def langsCreate():
    lang = {'name': request.json['name']}
    languages.append(lang)
    return jsonify({'languages': languages})

@app.route('/langs/<string:name>', methods=['PUT'])
def langsEdit(name):
    langs = [lang for lang in languages if lang['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify({'language': langs[0]})

@app.route('/langs/<string:name>', methods=['DELETE'])
def langsRemove(name):
    lang = [lang for lang in languages if lang['name'] == name]
    languages.remove(lang[0])
    return jsonify({'languages': languages})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
