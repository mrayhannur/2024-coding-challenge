# 2024 Coding Challenge
# February 1, 2024 (14/366)
# https://www.codewars.com/kata/554b4ac871d6813a03000035/

# Testcase: test.assert_equals(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"), "42 -9");

# My Own
def high_and_low(numbers):
    list = [int(i) for i in numbers.split(' ')]
    ordered_list = sorted(list)
    return str(ordered_list[-1]) + " " + str(ordered_list[0])

# Forum Best Answer
# 1
def high_and_low(numbers):
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

# 2
def high_and_low(numbers):
  numbers = [int(c) for c in numbers.split(' ')]
  return f"{max(numbers)} {min(numbers)}"