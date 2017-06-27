import hello

from colorama import Fore, Style

def test_format():
    assert hello.format('') == Fore.GREEN + Style.RESET_ALL
