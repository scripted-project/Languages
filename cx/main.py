from programs.cxc.x86_64_windows.main import cxc
from programs.cxi.x86_64_windows.main import cxi
from programs.cxt.x86_64_windows.main import cxt

from os import path, listdir, system, getcwd
import platform

def clear():
    if platform.system() == "Windows":
        system('cls')
    if platform.system() == "Linux":
        system("clear")
def explore(root_dir):
    while True:
        clear()
        print("Chose a CX file:")
        print(f"Current directory: {root_dir}")

        files = [f for f in listdir(root_dir) if path.isfile(path.join(root_dir, f))]

        for file in files:
            print(f"[file] {file}")

        subdirs = [d for d in listdir(root_dir) if path.isdir(path.join(root_dir, d))]
        for subdir in subdirs:
            print(f"[directory] {subdir}")

        explore_next = input("\nEnter the name of the directory to explore (or 'exit' to quit): ")
        
        if explore_next.lower() == 'exit':
            break
        
        next_path = path.join(root_dir, explore_next)
        
        if path.isdir(next_path):
            root_dir = next_path
        elif path.isfile(next_path):
            return next_path
        else:
            print("Invalid directory. Please enter a valid directory name.")
class Styles:
    reset = "\033[0m"
    bold = "\033[1m"
    underline = "\033[4m"

    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    purple = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"

    bg_black = "\033[40m"
    bg_red = "\033[41m"
    bg_green = "\033[42m"
    bg_yellow = "\033[43m"
    bg_blue = "\033[44m"
    bg_purple = "\033[45m"
    bg_cyan = "\033[46m"
    bg_white = "\033[47m"

    bright_black = "\033[90m"
    bright_red = "\033[91m"
    bright_green = "\033[92m"
    bright_yellow = "\033[93m"
    bright_blue = "\033[94m"
    bright_purple = "\033[95m"
    bright_cyan = "\033[96m"
    bright_white = "\033[97m"

    bg_bright_black = "\033[100m"
    bg_bright_red = "\033[101m"
    bg_bright_green = "\033[102m"
    bg_bright_yellow = "\033[103m"
    bg_bright_blue = "\033[104m"
    bg_bright_purple = "\033[105m"
    bg_bright_cyan = "\033[106m"
    bg_bright_white = "\033[107m"

os = platform.system()
s = Styles

clear()
output = f"""
        {s.blue}CX Main{s.reset}
    {s.blue}Scripted Project{s.reset}
     {s.yellow}v0.0.1{s.reset} {s.yellow}Testing{s.reset}
    
{s.blue}[A]{s.reset} C eXpanded Complier
{s.blue}[B]{s.reset} C eXpanded Interpreter
{s.blue}[C]{s.reset} C eXpanded Terminal
{s.blue}[D]{s.reset} Report Issue
{s.blue}[E]{s.reset} About CX Main
{s.blue}[F]{s.reset} Exit CX Main
"""
print(output)
user_input = input("Chose 1 of 6 options: ")

if user_input == "A":
    clear()
    output_path = input("Output path: (local for local directory)")
    if output_path == "local":
        output_path = f"{getcwd()}\output.bin"
    #cxc(explore(getcwd()))
    print("Finished!")

if user_input == "E":
    pass