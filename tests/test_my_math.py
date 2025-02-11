import pytest

from src.my_math import sum, multiply, difference, absolute_sum, calculate_birth_year

def test_sum():
    res = sum(1,1)
    assert res == 2

# Work together
## Test multiply
def test_multiply():
    assert multiply(2, 4) == 8
    assert multiply(-2, 5) == -10
    assert multiply(0, 17) == 0
    assert multiply(-2, -3) == 6

# Check for understanding
## Test difference
def test_difference():
    assert difference(5, 4) == 1
    assert difference(3, 6) == -3
    assert difference(0, 0) == 0
    assert difference(-3, -8) == 5

# Work together
## Test absolute sum
def test_absolute_sum():
    assert absolute_sum(-10, 5) == 15
    assert absolute_sum(10, -5) == 15
    assert absolute_sum(-10, -5) == 15
    assert absolute_sum(10, 5) == 15


# Check for understanding
## Test calculate age
def test_calculate_birth_year():
    assert calculate_birth_year(2025, 26, True) == 1999
    assert calculate_birth_year(2025, 26, False) == 1995
    assert calculate_birth_year(2025, 1, True) == 2024
    assert calculate_birth_year(2025, 1, False) == 2025
