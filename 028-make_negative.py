# 2024 Coding Challenge
# February 7, 2024 (28/366)
# https://www.codewars.com/kata/55685cd7ad70877c23000102/

# Testcase: 1 -> -1 ; 0 -> 0 ; -9 -> -9

# My Own
def make_negative( number ):
    return number*-1 if number > 0 else number

# Forum Best Answer
def make_negative( number ):
    return -abs(number)