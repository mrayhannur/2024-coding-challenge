# 2024 Coding Challenge
# February 2, 2024 (15/366)
# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

# My Own
def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        flag = 0
        for j in range(0, len(sub_string)):
            if i+len(sub_string) <= len(string):
                if string[i+j] == sub_string[j]:
                    flag += 1
                    
        if flag == len(sub_string):
            count+=1
            
    return count

# Forum Best Answer
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count