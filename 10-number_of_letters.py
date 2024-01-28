# 2024 Coding Challenge
# January 29, 2024 (10/366)
# https://www.codewars.com/kata/599febdc3f64cd21d8000117/

# Testcase: test.assert_equals(numbers_of_letters(1), ["one", "three", "five", "four"])
# Testcase: test.assert_equals(numbers_of_letters(999), ["nineninenine", "onetwo", "six", "three", "five", "four"])

# My Own
def numbers_of_letters(n):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    list = []
    string = 'this is just a template'

    # Loop to ensure the length of the string is below 9 (so it can access the words list index)
    while len(string) > 9:
        digits = [int(x) for x in str(n)]
        string = ''
        for digit in digits:
            string += words[digit]
        list.append(string)
        n = len(string)
    
    # Looping to get string 'four'
    while not 'four' in list:
        string = words[len(string)]
        list.append(string)
        
    return list

# Forum Best Answer
NUM = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def numbers_of_letters(n):
    s = ''.join(NUM[i] for i in map(int, str(n)))
    return [s] + (numbers_of_letters(len(s)) if len(s) != n else [])
