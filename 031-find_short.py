# 2024 Coding Challenge
# February 11 , 2024 (31/366)
# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/

# Testcase: test.assert_equals(find_short("lets talk about javascript the best language"), 3)
# Testcase: test.assert_equals(find_short("i want to travel the world writing code one day"), 1)

# My Own
def find_short(s):
    list_s = s.split(" ")
    l = min([len(word) for word in list_s])
    return l

# Forum Best Answer
def find_short(s):
    return min(len(x) for x in s.split())