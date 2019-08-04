"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""
# n = int(input('Please enter number of elements to add: '))
n = 10
el = 1                      # elements
result = 0
for _ in range(n):
    result = result + el
    el = el * -0.5
print(f'Cycle result: {result}')


def sum_rec(n, el, result):         # recursion
    if n == 0:
        return result
        result = result + el
    return sum_rec(n-1, el*-0.5, result)

print(f'Recursion result: {sum_rec(n, el, result)}')