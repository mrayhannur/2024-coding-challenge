# 2024 Coding Challenge
# February 5, 2024 (23/366)
# https://www.codewars.com/kata/58c9322bedb4235468000019/

# Instruction:
'''
number = 88 => returns false -> 8 + 8 = 16 -> 1 + 6 = 7 => 7 is odd 

number = 222 => returns true -> 2 + 2 + 2 = 6 => 6 is even

number = 5 => returns false

number = 841 => returns true -> 8 + 4 + 1 = 13 -> 1 + 3 => 4 is even
'''

# My Own
def is_very_even_number(n):
    while n > 9:
        list = [int(x) for x in str(n)]
        n = sum(digit for digit in list)
    
    return True if n % 2 != 1 else False

# Forum Best Answer
# 1
def is_very_even_number(n):
    while len(str(n)) > 1:
        n = sum(int(x) for x in str(n))
    return True if n % 2 == 0 else False

# 2
def is_very_even_number(n):
    return n == 0 or (n - 1) % 9 % 2
    # any number % 9 turns it into single digit (that sum of the digit)
    # ex: 14 % 9 = 5, which is (1+4)