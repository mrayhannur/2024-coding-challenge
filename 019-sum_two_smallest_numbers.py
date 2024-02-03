# 2024 Coding Challenge
# February 3, 2024 (19/366)
# https://www.codewars.com/kata/558fc85d8fd1938afb000014/

# Testcase: test.assert_equals(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
# Testcase: test.assert_equals(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)

# My Own
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

# Forum Best Answer
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])