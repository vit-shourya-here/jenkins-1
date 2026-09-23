import pytest
from app import add,sub

def test_add():
    assert add(9,9) == 18
def test_sub():
    assert sub(9,9) == 0