import pytest

def func(x):
    return x + 5

def test_method():
    assert func(3) == 5



#
# @Pytest.Fixture
# def numbers():
#     a = 10
#     b = 20
#     c = 30
#     return [a, b, c]
#
# def test_method_1(numbers):
#     x = 15
#     assert numbers[0] == x