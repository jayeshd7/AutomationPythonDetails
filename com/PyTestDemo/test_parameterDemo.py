

import pytest

import pytest


def sum(a, b):
    return a+b

@pytest.mark.parametrize("input1, input2, output",

                         [
                             (2, 3, 5),
                             (3, 3, 6),
                             (1, 1, 2)

                         ]
                         )
def test_cal_sum_1(input1, input2, output):
    result = sum(input1, input2)
    assert result == output


