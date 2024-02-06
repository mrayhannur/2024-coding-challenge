# 2024 Coding Challenge
# February 6, 2024 (27/366)
# https://www.codewars.com/kata/52597aa56021e91c93000cb0/

# Desc:  Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
# Example:  move_zeros([1, 0, 1, 2, 0, 1, 3]) -> returns [1, 1, 2, 1, 3, 0, 0]

# My Own
def move_zeros(lst):
    for element in lst:
        if element == 0:
            lst.append(element)
            lst.remove(element)
    return lst

# Forum Best Answer
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))