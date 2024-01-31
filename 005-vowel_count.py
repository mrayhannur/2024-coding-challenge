# 2024 Coding Challenge
# January 28, 2024 (5/366)
# https://www.codewars.com/kata/54ff3102c1bad923760001f3/

# My Own
def get_count(sentence):
    counter = 0
    for letter in sentence:
        if letter in ['a', 'i', 'u', 'e', 'o']:
            counter+=1
    return counter

# Forum Best Answer
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")