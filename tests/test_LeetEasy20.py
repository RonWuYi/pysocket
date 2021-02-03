import os
import sys
import pathlib

sys.path.insert(1, os.path.join(pathlib.Path(os.path.dirname(__file__)).parents[0], "LeetCode"))

from LeetEasy20 import isValid

def test_isValid01():
    assert isValid("()[]{}}{") == False

def test_isValid02():
    assert isValid("()[]{}") == True