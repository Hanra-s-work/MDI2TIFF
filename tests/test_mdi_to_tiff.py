# tests/test_ask_question.py

"""
File in charge of testing the functions contained in the class
"""

from sys import stderr
import mdi2img


def print_debug(string: str = "") -> None:
    """ Print debug messages """
    debug = False
    if debug is True:
        print(f"DEBUG: {string}", file=stderr)
