# 2024 Coding Challenge
# February 1, 2024 (12/366)
# https://www.codewars.com/kata/5a360620f28b82a711000047/

# My Own
def define_suit(card):
    # Check last character of the string to define the suit of the card
    if card[-1] == 'C':
        return 'clubs'
    elif card[-1] == 'D':
        return 'diamonds'
    elif card[-1] == 'H':
        return 'hearts'
    else:
        return 'spades'
    
# Forum Best Answer
def define_suit(card):
    d = {'C': 'clubs', 'S':'spades', 'D':'diamonds','H':'hearts'}
    return d[card[-1]]