## Question B
# The goal of this question is to write a software library 
# that accepts 2 version string as input and returns whether 
# one is greater than, equal, or less than the other. 
# As an example: “1.2” is greater than “1.1”. 
# Please provide all test cases you could think of.

class ComparisonsBetweenTwoStrings():
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

        if not (isinstance(str1, str) and isinstance(str2, str)):
            raise TypeError('Pass two strings as arguments.')

    def are_they_equal(self):
        if self.str1 == self.str2:
            return '"{}" is equal to "{}"'.format(self.str1, self.str2)
        else:
            return '"{}" and "{}" are differents'.format(self.str1, self.str2)

    def which_is_greater(self):
        s = [self.str1, self.str2]
        s.sort(reverse=True)

        return ('"{}" is greater than "{}"'.format(s[0], s[1]))
        
    def which_is_lesser(self):
        s = [self.str1, self.str2]
        s.sort()

        return ('"{}" is lesser than "{}"'.format(s[0], s[1]))