import unittest
from hamcrest import *
from lambdaFunctions import *


class TestLambdaFunctions(unittest.TestCase):

    def test_if_square_is_returning_correct_value(self):
        assert_that(square(3), is_(equal_to(9)))

    def test_if_pythagoras_test_is_working_fine(self):
        assert_that(sqrtOfSumOfSquares(3, 4), is_(equal_to(5)))

    def test_average_function_is_returning_correct_value(self):
        assert_that(avg(1, 2, 3), is_(equal_to(2)))