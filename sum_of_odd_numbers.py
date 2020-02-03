# Sum of odd numbers
# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python

# Instructions:
# Given the triangle of consecutive odd numbers:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...

# Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8

def row_sum_odd_numbers(n):
    return (n**3)

print(row_sum_odd_numbers(1))
print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(13))
print(row_sum_odd_numbers(41))

# Tests for code wars
# # Test.assert_equals(row_sum_odd_numbers(1), 1)
# # Test.assert_equals(row_sum_odd_numbers(2), 8)
# # Test.assert_equals(row_sum_odd_numbers(13), 2197)
# # Test.assert_equals(row_sum_odd_numbers(19), 6859)
# # Test.assert_equals(row_sum_odd_numbers(41), 68921)