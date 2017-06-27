import json
import os

from colorama import init, Fore, Back, Style

path =os.path.dirname(__file__)

with open(os.path.join(path, 'greeting.json')) as f:
    greeting = json.load(f)

def hello():
    print(Fore.GREEN + greeting + Style.RESET_ALL)

if __name__ == '__main__':
    hello()
