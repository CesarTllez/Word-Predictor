from flask import Flask, jsonify, request
from flask_cors import CORS

import main

app = Flask(__name__)
CORS(app)

@app.route('/api/suggestion/<string:word>', methods=['GET'])
def greet(word):
    suggestion = main.getSuggestion(word)
    return jsonify({
        'word': word,
        'suggestion': suggestion
    })

if __name__ == '__main__':
    app.run(
        debug = 'True',
        host = 'localhost',
        port = '5001'
    )