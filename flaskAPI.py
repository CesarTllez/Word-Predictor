from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/suggestion/<string:word>', methods=['GET'])
def greet(word):
    return jsonify({
        'message': word
    })

if __name__ == '__main__':
    app.run(
        debug = 'True',
        host = '192.168.0.12',
        port = '5001'
    )