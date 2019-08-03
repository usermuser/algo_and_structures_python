"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

data = int(input('Please enter number: '))

odd = 0
even = 0

for i in str(data):
    if int(i) % 2 == 0:
        print(f'{i} is Even')
        even += 1
    else:
        print(f'{i} is Odd')
        odd += 1

print(f'The number of even={even} and odd={odd}')
