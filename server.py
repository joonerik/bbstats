import flask
import random
import json
from flask import jsonify
from flask import request
from flask import send_from_directory
import csv

app = flask.Flask(__name__)
# app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def get():
    return '''
    <h3>POST /answers/user_id</h3>
    <h3>GET /stats/<h3>
    '''


@app.route('/answers/<name>', methods=['GET', 'POST'])
def answers(name):
    if request.method == 'GET':
        data = open(f'answers/{name}.json', 'rb').read()
        return json.loads(data)

    elif request.method == 'POST':
        data = request.get_json()
        print(data)
        content = json.loads(open(f'stats/joon.json', 'rb').read())
        # Add the new answer from POST to current JSON
        content["worldle"].append(data)

        with open(f'stats/{name}.json', 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=4)
        return f"Data for {name} updated!"


@app.route('/stats', methods=['GET'])
def stats():
    question_data = open('stats/joon.json', 'rb').read()
    question_data = json.loads(question_data)
    for question in question_data:
        print(question)
    return "Question not found!"