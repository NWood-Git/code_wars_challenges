# Code Wars: Create Phone Number
# https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

# Instructions:
# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
# Example:

# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!


def create_phone_number(n):
    str_num = [str(x) for x in n]
    num_list1 = str_num[0:3]
    num_list2 = str_num[3:6]
    num_list3 = str_num[6:]
    return f"({''.join(num_list1)}) {''.join(num_list2)}-{''.join(num_list3)}"

n = [1,2,3,4,5,6,7,8,9,0]

print(create_phone_number(n))
