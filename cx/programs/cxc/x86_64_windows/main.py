import json
from scripts.tokenizer import identify, tag

def hexadecimal(input_value):
    if isinstance(input_value, int):
        return input_value.to_bytes((input_value.bit_length() + 7) // 8, 'big') + b'\x0D\x0A'
    elif isinstance(input_value, float):
        int_value = int(input_value)
        return int_value.to_bytes((int_value.bit_length() + 7) // 8, 'big') + b'\x0D\x0A'
    elif isinstance(input_value, str):
        result = b""
        for char in input_value:
            try:
                result += ord(char).to_bytes(1, 'big')
            except ValueError:
                # Handle non-convertible characters
                result += bytes(f"Cannot convert '{char}' to ASCII. ", 'utf-8')
        return result + b'\x0D\x0A'
    else:
        return bytes(f"Unsupported type: {type(input_value)}. Input should be an integer, a float, or a string.", 'utf-8')

mcrefile = open("cx/data/mcref.json")
mc_ref = json.load(mcrefile)

tkrefile = open("cx/data/tokens.json")
tk_ref = json.load(tkrefile)

def cxc(input_path, output_path):
    output = open(output_path, 'wb')
    input = open(input_path, 'r')
    
    try:
        lines = {}
        i = 1
        for line in input.readlines():
            tagged = tag(line)
            lines[str(i)] = {
                "line": i,
                "tokens": identify(line),
                "tag": tagged if tagged is not None else None
            }
            if lines[str(i)]["tag"] == None: return 500
            i += 1
            
    except Exception as e:
        pass