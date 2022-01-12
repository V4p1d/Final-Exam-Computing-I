'''
GeneralProgramming.py



Functions performing operations on basic Python data structures.

TOTAL POINTS AVAILABLE: 40 (notice that each exercise has its own weight, specified under the examples)


1 * weight points -  The program works flawlessly and the appropriate ideas to solve it, have been used.

0.75 * weight points - The student has understood the logic and the program works for most inputs.
The code could use some improvement or it is very hard to read. The appropriate ideas to solve the problem have been used.

0.5 * weight points - The student has understood the logic but there are some major bugs, or the program is incomplete. 
This score is also assigned for programs that execute as intended but in a 
very inefficient way (for instance, using a very long list of if statements 
when the problem could be solved easily with a loop).

0.25 * weight points -  The student has attempted to solve the exercise but, either there is a 
logical error in the program (e.g., wrote something but it wouldn't solve the problem) 
or the program is largely incomplete.

0 points - The student has not attempted to solve the exercise or missed the point entirely 
(e.g., blank page or solved something unrelated to the question).
'''

# Write a function that accepts two integers as an input. The function will return
# a list of all the numbers n between a and b (a and b included), such that every digit in n is even.
# for example:
# given as inputs  a = 2, b = 27
# the function will return [2, 4, 6, 8, 20, 22, 24, 26] 
# notice that, for instance in 14, 1 is odd and 4 is even, therefore 14 is not added to the list
# WEIGHT = 8

def evenDigits():
    return