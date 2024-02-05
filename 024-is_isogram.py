# 2024 Coding Challenge
# February 6, 2024 (24/366)
# https://www.codewars.com/kata/54ba84be607a92aa900000f1/

# Desc: An isogram is a word that has no repeating letters, consecutive or non-consecutive
# Testcase: test.assert_equals(is_isogram("isogram"), True )
# Testcase: test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent" )

# My Own
def is_isogram(string):
    str_low = string.lower()
    x = list(str_low)
    y = set(x)

    return True if len(x) == len(y) else False 

# Forum Best Answer
# 1
def is_isogram(string):
    return len(string) == len(set(string.lower()))

# 2
def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True