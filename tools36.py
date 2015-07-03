__author__ = 'hoby'

def IsPalindromic(num):
    num_convert = str(num)
    new_num = num_convert[::-1]
    if new_num == num_convert:
        return num

def convert_binary(number):
    remaining = []
    while number > 0:
        rem = number % 2
        remaining.append(rem)
        number = number // 2
    rev_remaining = list(reversed(remaining))
    binary = "".join(map(str, rev_remaining))
    return binary