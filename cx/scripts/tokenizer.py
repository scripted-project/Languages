from nltk.tokenize import word_tokenize
import json

f = open("cx/data.json")
data = json.load(f)

class Tokenizer:
    def lex(self, source: str):
        tokens = word_tokenize(source)
        identifed = []
        
        for token in tokens:
            for type in data["types"]:
                if token in type["tokens"]: 
                    identified.append((token, type["name"]))
                    continue
                
                
                
        