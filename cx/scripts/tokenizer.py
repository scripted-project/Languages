from nltk.tokenize import word_tokenize
import json
import re

f = open("cx/data/tokens.json")
data = json.load(f)

def tokenize(input_string):
    # Keep 2 char combos combined without brackets
    input_string = re.sub(r'(\+\=\<[^>]*\>)', r'\1', input_string)
    # Keep 2 char combos combined with brackets
    input_string = re.sub(r'(\+\=|\-\=|\-\>|->)', r'\1', input_string)
    # Keep brackets combined
    input_string = re.sub(r'(\[.*?\])', r'\1', input_string)
    # Keep periods with stuff
    input_string = re.sub(r'(\w+)\.(\w+)', r'\1.\2', input_string)

    # Tokenize based on whitespace
    tokens = re.findall(r'\S+|\[.*?\]', input_string)

    return tokens

def extract_content(input_string, start_delimiter, end_delimiter):
    start_index = input_string.find(start_delimiter)
    end_index = input_string.find(end_delimiter, start_index + len(start_delimiter))
    
    if start_index != -1 and end_index != -1:
        return input_string[start_index + len(start_delimiter):end_index]
    else:
        return None
            
def cut_off_string(original_string, start_delimiter, end_delimiter):
    start_index = original_string.find(start_delimiter)
    end_index = original_string.find(end_delimiter, start_index + len(start_delimiter))
    
    if start_index != -1 and end_index != -1:
        return original_string[:start_index] + original_string[end_index + len(end_delimiter):]
    else:
        return original_string
    
def extract_content_between_brackets(input_string):
    found_first = False
    found_last = False
    string = []
    for char in input_string:
        if char == "<" and found_first == False:
            found_first = True
        elif found_first == True:
            if char == ">":
                break
            string.append(char)
        
    return "".join(string)
    
def identify(source: str):
    tokens = tokenize(source)
    identified = []

    i = 0
    while i < len(tokens):
        for context_key, context in data["contexts"].items():
            context = tokenize(context)
            if cut_off_string(context[0], "<", ">") == tokens[i]: # first word match
                j = 0
                for ctx_token in context:
                    identified.append((tokens[i + j], extract_content_between_brackets(ctx_token)))
                    j += 1
                i += j - 1        
                    
        i += 1
    return identified