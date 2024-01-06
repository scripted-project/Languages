import scripts.tokenizer as tk

def run(path):
    with open(path, 'r') as file:
        lines = file.readlines()

#print(tk.tokenize("callback<KEYWORD> [CALLBACK.ACTION] +=<ASSIGNMENT.OPERATOR> ctx<VARIABLE> -><CALLBACK.SIGN> [CALLBACK]"))
#print(tk.tokenize("callback action += ctx -> func"))
#print(tk.extract_content_between_brackets("callback<KEYWORD>"))
print(tk.identify("func string tostring()"))