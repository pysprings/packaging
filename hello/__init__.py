import json
import os

from colorama import init, Fore, Back, Style

path =os.path.dirname(__file__)

with open(os.path.join(path, 'greeting.json')) as f:
    greeting = json.load(f)

def format(line):
    return Fore.GREEN + line + Style.RESET_ALL

def hello():
    print(format(greeting))

if __name__ == '__main__':
    hello()
