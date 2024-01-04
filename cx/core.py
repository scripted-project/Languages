import json

import scripts.keywords as keywords 
import scripts.tokenizer as tk

f = open("cx/data.json")
data = json.load(f) 

def run(path):
    with open(path, 'r') as file:
        lines = file.readlines()

print(tk.tokenize("action += ctx -> func"))