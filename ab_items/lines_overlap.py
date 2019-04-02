## Question A
# Your goal for this question is to write a program that accepts two 
# lines (x1,x2) and (x3,x4) on the x-axis and returns 
# whether they overlap.
# As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

TYPE_ERROR_MSG = 'Pass tuples of int or float as input.'

def two_lines_overlap(line1, line2):
    _verify_tuple(line1, line2)

    x1, x2 = line1
    x3, x4 = line2

    _verify_number(x1, x2, x3, x4)

    if (x1 <= x3 and x3 <= x2) or (x3 <= x1 and x1 <= x4):
        return 'Overlap'
    else:
        return 'No Overlap'
    
def _verify_tuple(line1, line2):
    if not (isinstance(line1, tuple) and isinstance(line2, tuple)):
        raise TypeError(TYPE_ERROR_MSG)

def _verify_number(*args):
    for n in args:
        if not isinstance(n, (int, float)):
            raise TypeError(TYPE_ERROR_MSG)