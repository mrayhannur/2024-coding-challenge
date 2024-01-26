def enough(cap, on, wait):
    # Calculate the remaining seats available
    rem = cap - on
    
    # Validate the result
    if rem >= wait:
        # if the remaining seats available are sufficient for the number waiting
        return 0
    else:
        # if not
        return wait-rem # the number of people who didn't get in