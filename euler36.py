__author__ = 'hoby'

def IsPalindromic(num):
    num_convert = str(num)
    new_num = num_convert[::-1]
    if new_num == num_convert:
        return num
    #     print 'The number is palindromic'
    # else:
    #     print 'The number is not palindromic'


#print Palindromic
#print IsPalindromic(121)
#print int(str(32), base=10)


def convert_binary(number):
    remaining = []
    while number > 0:
        rem = number % 2
        remaining.append(rem)
        number = number // 2
    #print remaining
    rev_remaining = list(reversed(remaining))
    binary = "".join(map(str, rev_remaining))
    #num_binary = int(binary[::1])
    return binary

#print convert_binary(4)
# print convert_binary(2)


def main(end):
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

print main(1000000)

