# 2024 Coding Challenge
# January 27, 2024 (3/366)
# https://www.codewars.com/kata/53dc54212259ed3d4f00071c

def sum_array(a):
    # Check whether the list is empty or not
    if len(a):
        # initialize the result variable
        sum = 0
        
        # do a loop for each number inside list and sum to the result variable 
        for n in a:
            sum += n
            
        return sum
    else:
        return 0