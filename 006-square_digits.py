# 2024 Coding Challenge
# January 28, 2024 (6/366)
# https://www.codewars.com/kata/546e2562b03326a88e000020/

# My Own
def square_digits(num):
    # Create a list that holds each element of the given integer by converting the integer to a string
    list = [int(x) for x in str(num)]
    
    # Initialize variable for the result
    result = ''
    
    # Iterate over each element in the list by squaring and concatenating it into the result string
    for digit in list:
        result += str(digit*digit)
        
    # Return it by converting back the string to integer
    return int(result)

# Forum Best Answer
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)
