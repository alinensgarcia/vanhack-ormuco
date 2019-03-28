## Question B
# The goal of this question is to write a software library 
# that accepts 2 version string as input and returns whether 
# one is greater than, equal, or less than the other. 
# As an example: “1.2” is greater than “1.1”. 
# Please provide all test cases you could think of.

def which_is_greater(s1, s2):
    if not (isinstance(s1, str) and isinstance(s2, str)):
        raise TypeError('Pass two strings as arguments.')
    
    if s1 == s2:
        print('"{}" is equal than "{}".'.format(
            s1, 
            s2))

        return
    
    strings = [s1, s2]
    strings.sort()

    print('"{}" is greater than "{}".'.format(
        strings[1], 
        strings[0]))
    
    # e o less?

def which_is_less(s1, s2):
    pass

def are_they_equal(s1, s2):
    pass

if __name__ == '__main__':
    which_is_greater('a', 'b')
    which_is_greater('b', 'a')
    which_is_greater('1.1', '1.2')
    which_is_greater('1.2', '1.1')
    which_is_greater('10.2', '1.1')
    which_is_greater('11.2', '112')
    # which_is_greater('11.2', 1)
    # which_is_greater('11.2')
    which_is_greater('1', '1')