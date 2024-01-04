from nltk.tokenize import word_tokenize
import json

f = open("cx/data.json")
data = json.load(f)


def lex(self, source: str):
    tokens = word_tokenize(source)
    identified = []
    i = 0
    for token in tokens:
        for type in data["types"]:
            if token in type["tokens"]: 
                identified.append((token, type["name"]))
                continue
        
        for context in data["contexts"]:
            pattern = word_tokenize(context)
            first = 0
            vars = []
            definites = []
            n = 0
            for token in pattern:
                if not token.startswith("[") and not token.endswith("]"): #these dont exist
                    first = n
                elif token.startswith("[") and token.endswith("]"):
                    vars.append(token)
                n += 1
            if pattern[first] == tokens[i + first]:
                j = 0
                for token in pattern:
                    pass # align tokens then set them to each other and add i * len(pattern)
                
                
