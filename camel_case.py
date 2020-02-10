# CamelCase Method - Solved - 2/10/2020
# https://www.codewars.com/kata/587731fda577b3d1b0001196/train/python

# Instructions:
# Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings.
# All words must have their first letter capitalized without spaces.

# For instance:

# camelcase("hello case") => HelloCase
# camelcase("camel case word") => CamelCaseWord

def camel_case(string):
    string = string.title()
    return string.replace(' ', '')


print(camel_case("hello case")) #=> HelloCase
print(camel_case("camel case word")) #=> CamelCaseWord