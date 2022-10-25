from audioop import avg
import flask
import json
from flask import jsonify
from flask import request
from flask import send_from_directory
from flask import render_template
from system import getData

splitword = 'burger'

app = flask.Flask(__name__)
# app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def get():
    return render_template('form.html')

@app.route('/answers/<name>', methods=['GET', 'POST'])
def answers(name):
    if request.method == 'GET':
        data = open(f'answers/{name}.json', 'rb').read()
        dict = json.loads(data)

        all_headers = list(dict.keys())
        all_rows = list(zip(*dict.values()))
        
        return render_template('personScore.html', rows = all_rows, headers = all_headers, name = name)

    elif request.method == 'POST':
        text = request.form[f'burger_field_{name}']
        if not splitword in text:
            raise Exception(f"gimme {splitword}")
        else:
            stringArray = text.split(splitword)

        data = json.loads(getData(stringArray))
        content = json.loads(open(f'answers/{name}.json', 'rb').read())

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
    players.append(["joon", joonData])

    klitoData = open('answers/klito.json', 'rb').read()
    klitoData = json.loads(klitoData)
    players.append(["klito", klitoData])

    peteData = open('answers/pete.json', 'rb').read()
    peteData = json.loads(peteData)
    players.append(["pete", peteData])

    playerDict = {
        "joon":0,
        "klito":0,
        "pete":0
    }

    for player in players:
        dict = {
            "worldle": 0,
            "countryle": 0,
            "globle": 0,
            "tradle": 0,
            "flagle": 0
        }

        for item in player[1].items():
            avgNum = 0
            for e in item[1]:
                avgNum = avgNum + e
            if (len(item[1])):
                avgNum = avgNum / len(item[1])
            dict[item[0]] = avgNum
        playerDict[player[0]] = dict

    return f'''
        <h1>Average Scores</h1>
        <p>Joon: {playerDict["joon"]}</p>
        <br>
        <p>Klito: {playerDict["klito"]}</p>
        <br>
        <p>Pete: {playerDict["pete"]}</p>
        <br>
        <a href="/"><button>&#x2190; Tilbake</button></a>
    '''