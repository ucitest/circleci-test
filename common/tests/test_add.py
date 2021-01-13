__author__ = "Bagio Johnson"

from common.utils import add
import unittest


class Test():
    def setUp(self):
        pass

    def test_add_function(self):
        assert add(3,4) == 7
        assert add(3, 4) != 8
        print(
            'Hooray !!!!    '
            'All test cases were passed'
        )
