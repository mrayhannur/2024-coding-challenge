# 2024 Coding Challenge
# February 2, 2024 (16/366)
# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/

# Testcase: test.assert_equals(descending_order(15), 51)
# Testcase: test.assert_equals(descending_order(123456789), 987654321)

# My Own
def descending_order(num):
    list = [int(x) for x in str(num)]
    ordered_list = sorted(list, reverse=True)
    str_num = ''
    for num in ordered_list:
        str_num += str(num)
        
    return int(str_num)

# Forum Best Answer
def descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))