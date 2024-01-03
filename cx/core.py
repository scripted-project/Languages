import json
import scripts.keywords as keywords

f = open("cx/data.json")
data = json.load(f)


def run(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        