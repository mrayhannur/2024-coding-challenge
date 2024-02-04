# 2024 Coding Challenge
# February 5, 2024 (21/366)
# https://www.codewars.com/kata/515e271a311df0350d00000f/

#   test.assert_equals(square_sum([1,2]), 5)
#   test.assert_equals(square_sum([0, 3, 4, 5]), 50)

# My Own
def square_sum(numbers):
    res = 0
    for num in numbers:
        res += num*num
    return res

# Forum Best Answer
# 1
def square_sum(numbers):
    return sum(x ** 2 for x in numbers) # using power

# 2
def square_sum(numbers):
    return sum(x * x for x in numbers) 