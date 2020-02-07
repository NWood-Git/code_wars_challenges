# Replace With Alphabet Position - Solved 2/6/2020
# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.
# Example:
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

def remove_from_text(text):
    '''Removes non-letter characters from a string'''
    for item in text:
        if item.isalpha() == False:
            text = text.replace(item, '')
    return text

def alphabet_position(text):
    text = remove_from_text(text).lower()
    alphabet = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num_list = []
    for letter in text:
        num_list.append(str(alphabet.index(letter)+1))
    return ' '.join(num_list)

print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("zoo"))

# print(remove_from_text("The sunset sets at twelve o' clock."))
# alphabet = ['a', 'b','c', 'd', 'e']
# print(numbers)
# x = 'abcde'
# y = x.index('b')
# print(y)