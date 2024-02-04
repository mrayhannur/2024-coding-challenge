# 2024 Coding Challenge
# February 5, 2024 (22/366)
# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/

# test.assert_equals(accum("ZpglnRxqenU"), "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
# test.assert_equals(accum("NyffsGeyylB"), "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")

# My Own
def accum(st):
    string = ""
    st = list(st)
    for i in range (0, len(st)):
        for j in range(0, i+1):
            if j == 0:
                string += st[i].upper()
            else:
                string += st[i].lower()
        if i < len(st) - 1:
            string+='-'
    return string

# Forum Best Answer
# 1
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

# 2
def accum(s):
    output = ""
    for i in range(len(s)):
        output+=(s[i]*(i+1))+"-"
    return output.title()[:-1]