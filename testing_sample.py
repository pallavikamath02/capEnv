import pytest
def add1(x):
    return x+5
def test_method():
    assert add1(3)==5