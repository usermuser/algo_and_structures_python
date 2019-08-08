"""
2.	Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""
# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

t = tuple(i for i in range(2,100))              # 2 to 99
myrange = tuple(i for i in range(2,10))         # 2 to 9
c = 0    # our counter


def checker(num,myrange):
    _flag = False         # indicator that our number is a multiple of the entire range of numbers in myrange
    for i in myrange:
        if num % i == 0:
            _flag = True
                
        else:
            _flag = False
    return _flag

def is_even(num):
    if num % 2 == 0:
        return True
    

# Let's check all numbers in tuple t
even = []
for i in t:
    if checker(i,myrange):
        c += 1
    if is_even(i):     # task 2
        even.append(t.index(i))
        
print('So, {} numbers are multiple of each number in range 2 to 9'.format(c))
print('even indexes:', even)
