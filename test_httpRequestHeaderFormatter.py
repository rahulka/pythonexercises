from httpRequestHeaderFormatter import prettyPrintHeaders

import unittest
from hamcrest import *

class TestHTTPRequestFormatter(unittest.TestCase):

    def test_if_single_request_header_is_being_formatted_correctly(self):
        assert_that(prettyPrintHeaders(Content_Length=10), is_(equal_to("Content-Length:10\n")))

    def test_if_single_request_header_without_underscore_is_being_formatted_correctly(self):
        assert_that(prettyPrintHeaders(Accept="application/json"), is_(equal_to("Accept:application/json\n")))

    def test_if_single_request_header_with_multiple_underscores_is_being_formatted_correctly(self):
        assert_that(prettyPrintHeaders(If_Modified_Since="Sat, 29 Oct 1994 19:43:31 GMT"),
                    is_(equal_to("If-Modified-Since:Sat, 29 Oct 1994 19:43:31 GMT\n")))

    def test_if_multiple_request_headers_are_coming_in_new_line(self):
        assert_that(prettyPrintHeaders(Content_Length=10, Accept="application/json"),
                    is_(equal_to("Content-Length:10\nAccept:application/json\n")))

    def test_with_arbitrary_length_arguments(self):
        dict = {"Content_Length": 10, "Accept": "application/json"}
        assert_that(prettyPrintHeaders(**dict), is_(equal_to("Content-Length:10\nAccept:application/json\n")))
