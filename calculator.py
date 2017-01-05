"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here
while True:
    user_input = raw_input("Input expression to calculate: ")
    tokens = user_input.split()
    print tokens
    
    num_1=int(tokens[1])
    num_2=int(tokens[2])
    if tokens[0] == "q":
        break
    
    elif tokens[0] == "pow" and len(tokens) == 3:
        print power(num_1,num_2)
    elif tokens[0] == "+" and len(tokens) == 3 and type(tokens[1]) == int and type(tokens[2] == int):
        print add(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "-" and len(tokens) == 3 and type(tokens[1]) == int and type(tokens[2] == int):
        print subtract(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "*" and len(tokens) == 3 and type(tokens[1]) == int and type(tokens[2] == int):
        print multiply(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "/" and len(tokens) == 3 and type(tokens[1]) == int and type(tokens[2] == int):
        print divide(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "square" and len(tokens) == 2 and type(tokens[1]) == int:
        print square(int(tokens[1]))
    elif tokens[0] == "cube" and len(tokens) == 2 and type(tokens[1]) ==int:
        print cube(int(tokens[1]))
    elif tokens[0] == "mod" and len(tokens) == 3 and type(tokens[1]) == int and type(tokens[2] == int):
        print mod(int(tokens[1]), int(tokens[2]))
    else:
        print "Invalid input please choose one of the following operators +, -, *, /, square, cube, pow, mod or check the number arguments. Enter q to quit."
