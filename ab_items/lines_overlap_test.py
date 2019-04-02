import unittest
from lines_overlap import two_lines_overlap
 
class two_lines_overlap_test(unittest.TestCase):

    def test_wrong_input_tuple(self):
        try:
            two_lines_overlap(1, (1,2))
        except TypeError as e:
            result = e
        
        self.assertEqual(type(result), TypeError)

    def test_wrong_input_number(self):
        try:
            two_lines_overlap(('a', 'b'), ([1], [2]))
        except TypeError as e:
            result = e
        
        self.assertEqual(type(result), TypeError)

    def test_no_overlap(self):
        line1 = (1,2)
        line2 = (3,4)
        expected = 'No Overlap'

        self.assertEqual(two_lines_overlap(line1, line2), expected)

    def test_overlap_line1_before(self):
        line1 = (1,3)
        line2 = (2,4)
        expected = 'Overlap'
        
        self.assertEqual(two_lines_overlap(line1, line2), expected)

    def test_overlap_line1_after(self):
        line1 = (1,3)
        line2 = (2,4)
        expected = 'Overlap'
        
        self.assertEqual(two_lines_overlap(line2, line1), expected)

    def test_overlap_equal_lines(self):
        line1 = (1,3)
        line2 = (1,3)
        expected = 'Overlap'
        
        self.assertEqual(two_lines_overlap(line1, line2), expected)

    def test_overlap_lines_x1_equals_x3(self):
        line1 = (1,2)
        line2 = (1,3)
        expected = 'Overlap'
        
        self.assertEqual(two_lines_overlap(line1, line2), expected)

    def test_overlap_lines_x2_equals_x4(self):
        line1 = (1,4)
        line2 = (2,4)
        expected = 'Overlap'
        
        self.assertEqual(two_lines_overlap(line1, line2), expected)