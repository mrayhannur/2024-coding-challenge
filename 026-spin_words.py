# 2024 Coding Challenge
# February 6, 2024 (26/366)
# https://www.codewars.com/kata/5264d2b162488dc400000001/

# Desc:  returns the same string, but with all words that have five or more letters reversed
# Example:  "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# Example:  "This is a test        --> "This is a test" 

# My Own
def spin_words(sentence):
    str = ''
    l = list(sentence.split())
    for word in l:
        if len(word) >= 5:
            str += word[::-1] + " "
        else:
            str += word + " "

    return str[:-1]

# Forum Best Answer
def spin_words(sentence):
    return " ".join([word[::-1] if len(word) >= 5 else word for word in sentence.split(" ")])