# Unique In Order
# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

# Instructions
# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the 
# same value next to each other and preserving the original order of elements.
# For example:
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]


def unique_in_order(iterable):
    result = []
    for x in iterable:
        if result == []:
            result.append(x)
        elif x != result[-1]:
            result.append(x)
    return result

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print( unique_in_order([1,2,2,3,3]))


# #Old Answer ok but used range(len())

# def unique_in_order(iterable):
#     result = []
#     for idx in range(len(iterable)):
#         if idx == 0:
#             result.append(iterable[idx])
#         elif iterable[idx] != result[-1]:
#             result.append(iterable[idx])
#     return result