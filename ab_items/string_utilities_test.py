import unittest
from string_utilities import ComparisonsBetweenTwoStrings

class ComparisonsBetweenTwoStringsTest(unittest.TestCase):
    def test_wrong_arguments(self):
        try:
            ComparisonsBetweenTwoStrings('1', 2)
        except TypeError as e:
            result = e
        
        self.assertEqual(type(result), TypeError)

    def test_are_they_equal(self):
        c_equal = ComparisonsBetweenTwoStrings('1', '1')
        c_diff = ComparisonsBetweenTwoStrings('1', '2')
        
        expected_equal = '"{}" is equal to "{}"'.format(
                            c_equal.str1, c_equal.str2)
        expected_diff = '"{}" and "{}" are differents'.format(
                            c_diff.str1, c_diff.str2)

        self.assertEqual(c_equal.are_they_equal(), expected_equal)
        self.assertEqual(c_diff.are_they_equal(), expected_diff)

    def test_which_is_greater(self):
        str_lesser = '1'
        str_greater = '2'
        c = ComparisonsBetweenTwoStrings(str_greater, str_lesser)
        
        expected = '"{}" is greater than "{}"'.format(str_greater, str_lesser)

        self.assertEqual(c.which_is_greater(), expected)
        
    def test_which_is_lesser(self):
        str_lesser = '2'
        str_greater = '1'
        c = ComparisonsBetweenTwoStrings(str_greater, str_lesser)
        
        expected = '"{}" is lesser than "{}"'.format(str_greater, str_lesser)

        self.assertEqual(c.which_is_lesser(), expected)