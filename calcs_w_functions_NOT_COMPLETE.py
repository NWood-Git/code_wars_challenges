# Calculating with Functions - NEED TO COME BACK TO THIS ONE COULD NOT RESOLVE on 2/5/2020
# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

# Instructions:
# This time we want to write calculations using functions and get the results. Let's have a look at some examples:
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3

# Requirements:
#     There must be a function for each number from 0 ("zero") to 9 ("nine")
#     There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy
#     (divided_by in Ruby and Python)
#     Each calculation consist of exactly one operation and two numbers
#     The most outer function represents the left operand, the most inner function represents the right operand
#     Divison should be integer division. For example, this should return 2, not 2.666666...:

# eight(divided_by(three()))



def five(number=5,operation=0):
    if operation == None:
        return number
    else:
        return(operation(number, x=None))


def seven(number=7,operation=0):
    if operation == None:
        return number
    else:
        return(operation(number, x=0))

def plus(num1,num2):
    return num1 + num2

print(five(plus(seven())))
