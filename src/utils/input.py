from colorama import Fore

from ..utils.formatting import print_to_console
from .colors import LogColor


def get_user_input(question: str):
    print_to_console("Question", LogColor.GENERAL, question)
    i = input()
    return i
