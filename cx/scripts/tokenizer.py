from nltk.tokenize import word_tokenize
import json

f = open("cx/data.json")
data = json.load(f)

def tokenizer(*lines):
    pass

def identify(source: str):
    tokens = word_tokenize(source)
    identified = []
    i = 0
    while i < len(tokens):
        for type_key, type_info in data["types"].items():
            if tokens[i] in type_info["tokens"]:
                identified.append((tokens[i], type_info["name"]))
                break
        
        for context_key, context_pattern in data["contexts"].items():
            pattern_tokens = word_tokenize(context_pattern)
            vars = []
            definite = []

            for j, token in enumerate(pattern_tokens):
                if not token.startswith("[") and not token.endswith("]"):
                    definite.append((token, j))
                elif token.startswith("[") and token.endswith("]"):
                    vars.append((token, j))

            if i + j < len(tokens) and pattern_tokens[definite[0][1]] == tokens[i + j]:
                for j, token in enumerate(pattern_tokens):
                    for var in vars:
                        if var[1] == j:
                            identified.append((token, var[0][1:-1]))
                    for d in definite:
                        if d[1] == j:
                            identified.append((token, d[0][1:-1]))

                i += len(pattern_tokens) - 1

        i += 1
    return identified
                    
                