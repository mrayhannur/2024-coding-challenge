# 2024 Coding Challenge
# January 29, 2024 (7/366)
# https://www.codewars.com/kata/52fba66badcd10859f00097e/

# My Own
def disemvowel(string_):
    str = ''
    for letter in string_:
        if letter not in ['A', 'I', 'U', 'E', 'O', 'a', 'i', 'u', 'e', 'o']:
            str += letter
    return str

# Forum Best Answer
# 1
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

# 2
def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s