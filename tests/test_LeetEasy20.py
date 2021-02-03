import os
import sys
import pathlib

sys.path.insert(1, os.path.join(pathlib.Path(os.path.dirname(__file__)).parents[0], "LeetCode"))

from LeetEasy20 import isValid, isValid02

def test_isValid01():
    assert isValid("()[]{}}{") == False

def test_isValid02():
    assert isValid("()[]{}") == True
    
def test_isValid03():
    assert isValid("") == False

def test_isValid04():
    assert isValid02("([])[]{}") == True

def test_isValid011():
    assert isValid02("()[]{}}{") == False

def test_isValid021():
    assert isValid02("()[]{}") == True
    
def test_isValid031():
    assert isValid02(")") == False

def test_isValid041():
    assert isValid02("([])[]{}") == True