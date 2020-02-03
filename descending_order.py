# Descending Order
# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. 
# Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 21445 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321


def descending_order(num):
    str_test = str(num)
    num_list = []
    for x in range(len(str_test)):
        num_list.append(str_test[x])
    num_list = sorted(num_list, reverse=True)
    num_list = int(''.join(num_list))
    return (num_list)


test1 = 21445
test2 = 145263

print(descending_order(test1))
print(descending_order(test2))


