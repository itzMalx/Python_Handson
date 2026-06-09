import pytest
def test_sample_one():
    print("Hai")
def test_sample1():
    print("Welcome")
def test_sample2():
    print("Pytest")

def test_simple_assertion():
    assert 1+1==2

def test_equal_assertion():
    x=5
    y=5
    assert x==y
def test_not_equal_assertion():
    x=5
    y=10
    assert x!=y

def test_in_assertion():
    numbers=[1,2,3,4,5]
    assert 3 in numbers
    
def test_sample3():
    a="malu"
    b="malu"
    assert a.__eq__(b)
