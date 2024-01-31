# 2024 Coding Challenge
# January 29, 2024 (9/366)
# https://www.codewars.com/kata/64600b4bbc880643faa343d1/

# My Own
def get_dividers(values, powers):
    i = 0
    x = 1
    while i < len(values):
        x *= values[i] ** powers[i]
        i+=1

    dividers = []
    for i in range (1, x+1):
        if (x / i).is_integer():
            dividers.append(i)
    
    return dividers

# Forum Best Answer
# 1
from itertools import product
from operator import pow
from math import prod

def get_dividers(values, powers):
    return sorted(prod(map(pow, values, x)) for x in product(*(range(p+1) for p in powers)))

# 2
def get_dividers(values, powers):
    total = 1
    l = []
    for s in range(len(values)):
        total *= (values[s]**powers[s])
    for i in range(1,total+1):
        if total%i == 0:
            l.append(i)
    return l