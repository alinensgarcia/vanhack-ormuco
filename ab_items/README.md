# Exercise A
The lines_overlap.two_lines_overlap() funcion accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap.

Examples:
```python
>>> from lines_overlap import two_lines_overlap
>>> two_lines_overlap((1,2), (1,3))
'Overlap'
>>> two_lines_overlap((1,2), (3,4))
'No Overlap'
```

# Exercise B
A library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. 

Examples:
```python
>>> from string_utilities import ComparisonsBetweenTwoStrings
>>> c = ComparisonsBetweenTwoStrings('1','2')
>>> c.are_they_equal()
'"1" and "2" are differents'
>>> c.which_is_greater()
'"2" is greater than "1"'
>>> c.which_is_lesser()
'"1" is lesser than "2"'
>>> c = ComparisonsBetweenTwoStrings('b','a')
>>> c.are_they_equal()
'"b" and "a" are differents'
>>> c.which_is_greater()
'"b" is greater than "a"'
>>> c.which_is_lesser()
'"a" is lesser than "b"'
```

# Run automated tests
```
python3.6 -m unittest test_lines_overlap.py
python3.6 -m unittest test_string_utilities.py
```