# 2024 Coding Challenge
# February 1, 2024 (13/366)
# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/

# My Own (Check the item should integer)
def filter_list(l):
    integer_list = []
    for item in l:
        # Check the item's data type if it's integer or not
        if isinstance(item, int):
            integer_list.append(item)
    return integer_list # Return only the list of integer item

# Forum Best Answer (Check the item should not string)
def filter_list(l):
  # instruction: 'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]