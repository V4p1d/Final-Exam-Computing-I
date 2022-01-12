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

# Write a function that finds the longest palindrome in a list of words.
#   - if there is no palindrome word in the input list, the function will return None.
#   - if there are two or more palindrome words of the same length, return the first one in the list.
# Ignore punctuation and upper and lower cases. 
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward
# for example:
# from an input list of ["cat", "hello", "nun"]
# the function will return "nun"
# from an input list of ["cat", "hello", "nun", "never odd or even"]
# the function will return "never odd or even"
# WEIGHT = 8

def longestPalindrome():
    return