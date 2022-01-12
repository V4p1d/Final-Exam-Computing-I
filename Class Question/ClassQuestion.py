'''
ClassQuestion.py


TOTAL POINTS AVAILABLE: 50


8 points per method, 42 across whole class, 8 points for the creation of the students and the task.

--------------------------------------
Marking for methods:
--------------------------------------

8 points -  The program works flawlessly, it is commented and easy to read. The appropriate ideas to solve it, have been used.

6-7 points - The student has understood the logic and the program works for all inputs.
The code could use some improvement or it is difficult to read and understand. The appropriate ideas to solve the problem have been used.

4-5 points - The student has understood the logic and the program works for most inputs. 
The appropriate ideas to solve the problem have been used.

2-3 points - The student has understood the logic but there are some major bugs, or the program is incomplete. 
This score is also assigned for programs that execute as intended but in a 
very inefficient way (for instance, using a very long list of if statements 
when the problem could be solved easily with a loop).

1 points -  The student has attempted to solve the exercise but, either there is a 
logical error in the program (e.g., wrote something but it wouldn't solve the problem) 
or the program is largely incomplete.

0 points - The student has not attempted to solve the exercise or missed the point entirely 
(e.g., blank page or solved something unrelated to the question).

--------------------------------------
Marking for the creation of trolleys:
--------------------------------------

8 points -  The program works flawlessly, it is commented and easy to read. The appropriate ideas to solve it, have been used.

6-7 points - The student has understood the logic and the program works for all inputs.
The code could use some improvement or it is difficult to read and understand. The appropriate ideas to solve the problem have been used.

4-5 points - The student has understood the logic and the program works for most inputs. 
The appropriate ideas to solve the problem have been used.

2-3 points - The student has understood the logic but there is some major bugs, or the program is incomplete. 
This score is also assigned for programs that execute as intended but in a 
very inefficient way (for instance, using a very long list of if statements 
when the problem could be solved easily with a loop).

1 points -  The student has attempted to solve the exercise but, either there is a 
logical error in the program (e.g., wrote something but it wouldn't solve the problem) 
or the program is largely incomplete.

0 points - The student has not attempted to solve the exercise or missed the point entirely 
(e.g., blank page or solved something unrelated to the question).

'''



# Create a class called Trolley with one instance attribute called 'contents'
# that is created in the constructor. 
#     - 'contents' will be a dictionary and will start empty in the constructor
#        but when populated later by other methods: 
#         - the keys will be string describing the product (e.g. 'bread') 
#         - and the values will be a dictionary of two items
#                   1. the first item is 'cost' of a single product and 
#                   2. the second item is 'quantity' 
#                   (e.g. {'cost':1.50, 'quantity':3})


# Create a method called add_product(). It should:
#   - have 3 parameters: 'product_name', 'product_cost' and 'quantity'
#   - 'quantity' has a default value of 1
#   - it should add the product to the 'contents' attribute
#        - if the product exists already, increase the quantity accordingly and ignore
#          the product_cost if different than the one already in the dictionary
#        - if the product does not already exist in the dictionary, add a new entry


# Create a method called remove_product(). It should:
#   - have 2 parameters: 'product_name', 'quantity'
#   - it should reduce the quantity of the product in the 'contents' attribute
#        - if the product exists already, decrease the amount by 'quantity'
#        - if the product quantity becomes 0, remove the entry from the dictionary


# Create a method called change_price(). It should:
#   - have 2 parameters: 'product_name', 'price'
#   - it should change the price of the product "product_name" to "price", in the 'contents' attribute
#   - if the product "product_name" does not exist, add a new entry to 'contents'


# Create a method called calculate_cost(). It should:
#   - return the total value of the trolley (cost x quantity)



# Write a function called merge_trolley(). It should:
#   - have two parameters, both of which are trolley object, called 'trolley_1' and 'trolley_2'
#   - it should return a new trolley called 'other_trolley' that possesses all the items from
#     trolley_1 and trolley_2:
#       - if one entry already exists in the contents of both trolley_1 and trolley_2, 
#         sum the two quantities.
#       - if one entry that exist in both trolleys has a different price in trolley_1 than the 
#         price in trolley_2 then the function should return None and print "the two trolleys are
#         not compatible. Some prices are inconsistent.".
#       
#
# Notice that the total cost of the new created trolley should be equal to the sum of the cost
# of trolley_1 and the cost of trolley_2. Showcase that this is indeed the case by creating two
# instances of a trolley (with arbitrary items) and merging them with the function merge_trolley in 
# a new trolley. Print the cost of the three trolleys.