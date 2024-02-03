# 2024 Coding Challenge
# February 3, 2024 (20/366)
# https://www.codewars.com/kata/525f50e3b73515a6db000b83

# Testcase: test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
# Testcase: test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
# Testcase: test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")

# My Own
def create_phone_number(n):
    string = '('
    for i in range(0, len(n)):
        string += str(n[i])
        if i == 2:
            string += ') '
            
        if i == 5:
            string += '-'
    return string

# Forum Best Answer
# 1
def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# 2
def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])