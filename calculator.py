"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here
while True:
    input = raw_input("Input expression to calculate: ")
    tokens = input.split()
    
    if tokens[0] == "q":
        break
    
    elif tokens[0] == "pow" and len(tokens) == 3:
        print power(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "+" and len(tokens) == 3:
        print add(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "-" and len(tokens) == 3:
        print subtract(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "*" and len(tokens) == 3:
        print multiply(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "/" and len(tokens) == 3:
        print divide(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "square" and len(tokens) == 2:
        print square(int(tokens[1]))
    elif tokens[0] == "cube" and len(tokens) == 2:
        print cube(int(tokens[1]))
    elif tokens[0] == "mod" and len(tokens) == 3:
        print mod(int(tokens[1]), int(tokens[2]))
    else:
        print "Invalid input please choose one of the following operators +, -, *, /, square, cube, pow, mod or check the number arguments. Enter q to quit."
