# 2024 Coding Challenge
# January 27, 2024 (2/366)
# https://www.codewars.com/kata/5704aea738428f4d30000914/

def triple_trouble(one, two, three):
    # initialize the result variable
    string = ""
    
    # do a loop for each character index of each string 
    # (provided that all strings have the same length)
    for x in range(0, len(one)):
        # add each character for each string with every index alternately
        string += one[x]
        string += two[x]
        string += three[x]
    
    return string