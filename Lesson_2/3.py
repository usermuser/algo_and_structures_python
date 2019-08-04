"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

num = int(input('Please enter a number: '))

def rev(num):
    s = ''
    while num > 0:
        s += str(num%10)
        num = num // 10
    return s

print(f'Cycle result: {rev(num)}')


def recursion(num, s=''):
    if num < 1:
        return s
    s += str(num%10)
    return recursion((num // 10), s)


print(f'Recursion result: {recursion(num)}')

