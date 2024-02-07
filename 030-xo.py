# 2024 Coding Challenge
# February 7, 2024 (30/366)
# https://www.codewars.com/kata/55908aad6620c066bc00002a/

# Testcase: 
'''
test_cases = [
        ("ooxx",    True),
        ("xooxx",   False),
        ("ooxXm",   True), # Comparison is case-insensitive
        ("zpzpzpp", True), # when no 'x' and 'o' is present should return true
        ("zzoo",    False),
        ("oxOx",    True),
        ("",        True),  # Empty string contains equal amount of x and o
    ]
'''

# My Own
def xo(s):
    count_x, count_o = 0, 0
    for l in s.lower():
        if l == 'x':
            count_x += 1
        elif l == 'o':
            count_o += 1
            
    return count_x == count_o

# Forum Best Answer
def xo(s):
    return s.lower().count('x') == s.lower().count('o')