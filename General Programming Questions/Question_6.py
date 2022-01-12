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

# Write a function that accepts two string as inputs. 
# The first parameter will be a string of characters, and the second parameter 
# will be the same string of characters, but they will be in a different order 
# and have one extra character. The function should return that extra character.
#   - if the strings differ for more than two characters the function will return None
# for example:
# from inputs: "hello", "hollen"
# the function will return "n"
# from inputs: "hello", "hollenn"
# the function will return None
# WEIGHT = 5

def missingWord():
    return