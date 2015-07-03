__author__ = 'hoby'

from tools36 import *

def main3(end):
    palindromic = []
    palindromicBoth = []
    for i in range(end):
        if IsPalindromic(i):
            palindromic.append(i)
    for num in palindromic:
        bin = convert_binary(num)
        if IsPalindromic(bin):
            palindromicBoth.append(num)
    sum_num = sum(palindromicBoth)
    return sum_num
    #print sum_num

print main3(1000000)