from nltk.tokenize import word_tokenize
import json

f = open("cx/data.json")
data = json.load(f)

class Tokenizer:
    def lex(self, source: str):
        tokens = word_tokenize(source)
        identifed = []
        i = 0
        for token in tokens:
            for type in data["types"]:
                if token in type["tokens"]: 
                    identified.append((token, type["name"]))
                    continue
            
            for context in data["contexts"]:
                pattern = word_tokenize(context)
                first = 0
                n = 0
                for token in pattern:
                    if not token.startsWith("[") and not token.endsWith("]"): #these dont exist
                        first = n
                    n += 1
                if pattern[first] == tokens[i + first]:
                    for token in pattern:
                        token
                
                
                
        