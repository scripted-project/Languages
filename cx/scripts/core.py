from scripts.tokenizer import identify
from scripts.functions import Events, Functions

from nltk.tokenize import word_tokenize
from json import load

f = open("cx/data/tokens.json")
tk_data = load(f)

rax = None # words
rbx = None # types
rcx = None # tokens of function
rdx = None

var_reference = {}
func_reference = {}

events = Events()
functions = Functions()

def run_it(): # interactive terminal
    while True:
        try:
            user_input = input(">> ")
            if user_input in ["exit", "stop"]:
                break
            
            identified = identify(user_input)
            rax = []
            rbx = []
            
            i = 0
            while i < len(identified):
                rax.append(identified[i][0])
                rbx.append(identified[i][0])
                
            for ctx_key, ctx in tk_data["types"].items():
                if ctx["varstr"] == rbx:
                    rcx = word_tokenize(ctx["function"])
                    rdx = ""
                    rdx += rcx[0]
                    rdx += rcx[1]
                    
                    j = 2
                    while j < len(rcx):
                        if rcx[j] == "<":
                            k = 0
                            while k < len(rbx):
                                if rcx[j + 1] == rbx[k]:
                                    rdx += rax[k]
                        elif rcx[j] == ">":
                            pass
                        else:
                            rdx[j] += rcx[j]
                    eval(rdx)
        except Exception as e:
            print(e)