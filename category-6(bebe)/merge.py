import json

filenames = ['output(0-10^4).json', 'output(10^4-10^5).json', 'output(10^5-10^6).json', 'output(10^6-end).json']

data = []

for filename in filenames:
    with open(filename, 'r') as file:
        data.append(json.load(file))

with open('merge.json', 'w') as file:
    json.dump(data, file)