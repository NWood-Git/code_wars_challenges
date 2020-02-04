# Duplicate Encoder
# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears 
# only once in the original string, or ")" if that character appears more than once in the original string. 
# Ignore capitalization when determining if a character is a duplicate.
# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 
# Notes:
# Assertion messages may be unclear about what they display in some languages. 
# If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

def duplicate_encode(word):
    result = ''
    word = word.lower()
    for letter in word:
        if word.count(letter) == 1:
            result += '('
        else:
            result += ')'
    return result

print(duplicate_encode('din'))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))

# Used the below to check to make code

# print("recede".count('e'))

# x = ''
# x += '('
# x += '('
# print(x)