# 2024 Coding Challenge
# February 3, 2024 (17/366)
# https://www.codewars.com/kata/56747fd5cb988479af000028/

# Testcase: test.assert_equals(get_middle("test"),"es")
# Testcase: test.assert_equals(get_middle("testing"),"t")

# My Own
def get_middle(s):
    return s[len(s)//2] if len(s) % 2 == 1 else s[len(s)//2 - 1]+s[len(s)//2]

# Forum Best Answer
# 1
def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]

# 2
def get_middle(s):
    i = (len(s) - 1) // 2
    return s[i:-i] or s