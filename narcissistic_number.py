# Does my number look big in this?
# https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python

# Instructions:
# A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits in a given base.
# In this Kata, we will restrict ourselves to decimal (base 10).
# For example, take 153 (3 digits):
#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# and 1634 (4 digits):
#     1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
# The Challenge:
# Your code must return true or false depending upon whether the given number is a Narcissistic number in base 10.
# Error checking for text strings or other invalid inputs is not required, only valid integers will be passed into the function.

def narcissistic( value ):
    val = str(value)
    len_val = len(val)
    num_list = [int(x)**len_val for x in val]
    
    if sum(num_list) == value:
        return True #f'{value} is narcissistic'
    else:
        return False #f'{value} is  not narcissistic'

print(narcissistic(153))
print(narcissistic(1634))
print(narcissistic(7))
print(narcissistic(371))
print(narcissistic(122))
print(narcissistic(4887))
