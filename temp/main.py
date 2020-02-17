# from mongodb import *

from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return 'Server Works!'


@app.route('/greet')
def say_hello():
    return 'Hello from Server'


@app.route('/user', methods=['POST'])
def post_user():
    print(request.json)

    return jsonify(request.json)

@app.route('/user', methods=['GET'])
def get_user():
    data = {}
    data["bar"] = "foo"

    return jsonify(data)