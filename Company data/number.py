import json

with open('total(sch-1-4, pci-1-4).json', 'r') as file:
    data = json.load(file)

print(len(data))