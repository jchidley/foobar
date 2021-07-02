# https://foobar.withgoogle.com
# Level 2, Challenge 1
import pytest
from l2c1_in_work import *


def test_1():
    assert solution([2, 0, 2, 2, 0]) == "8"


def test_2():
    assert solution([-2, -3, 4, -5]) == "60"
