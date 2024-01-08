import json, threading
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

vardict = {}
funcdict = {}

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
            if "VARIABLE" in lines[str(i)]["tag"]:
                temp = []
                for token in lines[str(i)]["tokens"]:
                    if token[1] == "VARIABLE":
                        temp.append(token[0])
                        for token2 in lines[str(i)]["tokens"]:
                            if token2[1] == "VARIABLE.VALUE":
                                temp.append(token2[0])
                if len(temp) < 2: return 500
                vardict[temp[0]] = temp[1]
            i += 1
        
        assembly = """
        section .text
            global _start
        _start:
        """
        layers = 0
        for line_number, line_data in lines:
            if line_data["tag"] in mc_ref:
                assembly += f"; {line_number}: {line_data['tag']}\n"
                for line in mc_ref[line_data["tag"]]:
                    assembly += f"{'    ' * layers + 1}{line}\n"
                    
            
    except Exception as e:
        pass