# 2024 Coding Challenge
# February 3, 2024 (18/366)
# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/

# Testcase: test.assert_equals(find_next_square(121), 144, "Wrong output for 121")
# Testcase: test.assert_equals(find_next_square(155), -1, "Wrong output for 155")

# My Own
import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    x = math.sqrt(sq)
    result = -1 if x  % 1 != 0 else (x+1)**2
    return result

# Forum Best Answer
# 1
def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1

# 2
def find_next_square(sq):
    x = sq**0.5    
    return -1 if x % 1 else (x+1)**2