import json

def getData(answerArray):
    stringArray = answerArray
    #for line in answerString.splitlines():
    #    stringArray.append(line)

    dict = {
        "worldle": '',
        "countryle": '',
        "tradle": '',
        "globle": '',
        "flagle": ''
    }

    for line in stringArray:
        if '#Worldle' in line:
            if 'X' in line:
                dict["worldle"] = (6)
            else:
                dict["worldle"] = (int(line[line.index('/6')-1]))

        elif 'Guessed' in line:
            string = line.replace('Guessed in ', '')
            string = string.replace(' tries.', '')
            dict["countryle"] = (int(string))

        elif 'Gave up after' in line:
            string = line.replace('Gave up after ', '')
            string = string.replace(' tries.', '')
            dict["countryle"] = (int(string))

        elif '#Tradle' in line:
            if 'X' in line:
                dict["tradle"] = (6)
            else:
                dict["tradle"] = (int(line[line.index('/6')-1]))

        elif '=' in line:
            string = line.split('= ')[1]
            dict["globle"] = (int(string))
        
        elif '#Flagle' in line:
            dict["flagle"] = (int(line[line.index('/6')-1]))
    
    return json.dumps(dict)

with open('drit.txt') as f:
    #print(getData(f.read()))
    print("Kjøh")