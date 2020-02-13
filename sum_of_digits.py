# Sum of Digits / Digital Root - Solved 2/13/2020
# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
# Instructions:
# In this kata, you must create a digital root function.

# A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. 
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
# This is only applicable to the natural numbers.

def digital_root(n):
    st = str(n)
    lst = [int(i) for i in st]
    dig_sum = sum(lst)
    
    if dig_sum <= 9:
        # print(dig_sum)
        return dig_sum
    else:
        # print(dig_sum)
        return digital_root(dig_sum)
        

print(digital_root(1234))

# Time Complexity is n**2
# Space Complexity is n



# Here's how it works:

# digital_root(16)
# => 1 + 6
# => 7

# digital_root(942)
# => 9 + 4 + 2
# => 15 ...
# => 1 + 5
# => 6

# digital_root(132189)
# => 1 + 3 + 2 + 1 + 8 + 9
# => 24 ...
# => 2 + 4
# => 6

# digital_root(493193)
# => 4 + 9 + 3 + 1 + 9 + 3
# => 29 ...
# => 2 + 9
# => 11 ...
# => 1 + 1
# => 2