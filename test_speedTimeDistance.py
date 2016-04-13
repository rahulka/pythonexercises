from speedTimeDistance import calculatespeedtimedistance

import unittest
from hamcrest import *


class TestSpeedTimeDistance(unittest.TestCase):

    def test_speed_after_time_and_distance_is_given(self):
        assert_that(calculatespeedtimedistance(time=10, distance=10),
                    is_(equal_to({"speed": 1, "time": 10, "distance": 10})))

    def test_time_when_speed_and_distance_is_given(self):
        assert_that(calculatespeedtimedistance(speed=10, distance=10),
                    is_(equal_to({"speed": 10, "time": 1, "distance": 10})))

    def test_distance_when_speed_and_time_is_given(self):
        assert_that(calculatespeedtimedistance(speed=10, time=10),
                    is_(equal_to({"speed": 10, "time": 10, "distance": 100})))

    def test_if_method_raises_exception_when_only_speed_is_passed(self):
        assert_that(calling(calculatespeedtimedistance).with_args(speed=10),
                    raises(AttributeError, "Please pass at least two values among speed, time and distance."))

    def test_if_speed_is_correct_when_divison_is_not_integer(self):
        assert_that(calculatespeedtimedistance(time=3, distance=10)["speed"], is_(close_to(3.33, 0.01)))

    def test__with_arbitrary_length_arguments(self):
        dict = {"speed": 10, "time": 10}
        assert_that(calculatespeedtimedistance(**dict), is_(equal_to({"speed": 10, "time": 10, "distance": 100})))

