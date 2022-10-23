from audioop import avg
import flask
import random
import json
from flask import jsonify
from flask import request
from flask import send_from_directory
from system import getData
import csv

splitword = 'burger'

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
        text = request.get_data(as_text=True)
        
        if not splitword in text:
            raise Exception(f"gimme {splitword}")
        else:
            stringArray = text.split(splitword)

        data = json.loads(getData(stringArray))
        content = json.loads(open(f'answers/joon.json', 'rb').read())

        for game, score in data.items():
            content[game].append(score)

        with open(f'answers/{name}.json', 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=4)

        return f"Data for {name} updated!"

@app.route('/answers', methods=['GET'])
def stats():
    players = []

    joonData = open('answers/joon.json', 'rb').read()
    joonData = json.loads(joonData)
    players.append(joonData)

    klitoData = open('answers/klito.json', 'rb').read()
    klitoData = json.loads(klitoData)
    players.append(klitoData)

    peteData = open('answers/pete.json', 'rb').read()
    peteData = json.loads(peteData)
    players.append(peteData)

    dict = {
        "worldle": 0,
        "countryle": 0,
        "globle": 0,
        "tradle": 0,
        "flagle": 0
    }

    for player in players:
        for item in player.items():
            avgNum = 0
            for e in item[1]:
                avgNum = avgNum + e
            if (len(item[1])):
                avgNum = avgNum / len(item[1])
            dict[item[0]] = avgNum
            print(avgNum)

    print(dict)

    return "Question not found!"