# Find the unique number - Solved 2/7/2020
# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

# Instructions:
# There is an array with some numbers. All numbers are equal except for one. Try to find it!
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

# It’s guaranteed that array contains at least 3 numbers.
# The tests contain some very huge arrays, so think about performance.
# This is the first kata in series:
#     Find the unique number (this kata)
#     Find the unique string
#     Find The Unique

def find_uniq(arr): #optimal solution - big o of n
    if arr[0] != arr[1] and arr[0] != arr[2]:
        return arr[0]
    else:
        counter = 1
        for i in arr:
            if i ==  arr[counter]:
                counter += 1
            else:
                return arr[counter]

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print(find_uniq([0,1,1,1,1]))
print(find_uniq([7,9,9,9,9,9]))
print(find_uniq([9,7,9,9,9,9,9]))

# better but not optimal
def find_uniq2(arr): #big o of nlogn 
    arr = sorted(arr)
    if arr[0] != arr[1]:
        return arr[0]
    else:
        return arr[-1]
# print(find_uniq2([ 1, 1, 1, 2, 1, 1 ]))
# print(find_uniq2([ 0, 0, 0.55, 0, 0]))

# the below works but is times out on large datasets
def find_uniq1(arr): #big o of n^2
    for n in arr:
        if arr.count(n) == 1:
            return n
# print(find_uniq1([ 1, 1, 1, 2, 1, 1 ]))
# print(find_uniq1([ 0, 0, 0.55, 0, 0]))