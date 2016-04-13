from calculator import calculator

import unittest
from hamcrest import *
from operator import add, mul


class TestCalculator(unittest.TestCase):

    def test_if_zero_params_is_raising_an_exception(self):
        assert_that(calling(calculator).with_args(add), raises(TypeError))

    def test_if_passing_one_arg_is_returning_same_value(self):
        assert_that(calculator(add, 1), is_(equal_to(1)))

    def test_multiple_values_to_add(self):
        assert_that(calculator(add, 1, 2, 3, 4), is_(equal_to(10)))

    def test_multiple_values_to_multiplication(self):
        assert_that(calculator(mul, 1, 2, 3), is_(equal_to(6)))

    def test_mulitplication_with_arbitrary_variables(self):
        args = [1, 2, 3]
        assert_that(calculator(mul, *args), is_(equal_to(6)))

