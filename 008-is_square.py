# 2024 Coding Challenge
# January 29, 2024 (8/366)
# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/

# My Own
import math

def is_square(n):    
    if n >= 0:
        x = math.sqrt(n)
        return x * x == n
    return False

# Forum Best Answer
# 1
import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;

# 2
def is_square(n):    
    return n >= 0 and (n**0.5) % 1 == 0

# 3
import math
def is_square(n):    
    if n < 0:
        return False
    sqrt = math.sqrt(n)
    return sqrt.is_integer()
