from functionalExercises import fmax
from hamcrest import *
import unittest


class TestFunctionMax(unittest.TestCase):

    def test_with_zero_parameters_if_it_raises_exception(self):
        assert_that(fmax, raises(Exception, "Please pass 1 or more values to calculate values"))

    def test_with_only_one_value(self):
        assert_that(fmax(1), is_(equal_to(1)))

    def test_with_two_values(self):
        assert_that(fmax(1, 2), is_(equal_to(2)))

    def test_with_three_values(self):
        assert_that(fmax(1, 2, 3), is_(equal_to(3)))


if __name__ == "__main__":
    unittest.main()
