"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

# Your code goes here
while True:
    input = raw_input("Input expression to calculate: ")
    tokens = input.split(" ")
    if tokens[0] == "q":
        break
    else:
        if tokens[0] == "pow":
            print power(int(tokens[1]), int(tokens[2]))
        if tokens[0] == "+":
            print add(int(tokens[1]), int(tokens[2]))