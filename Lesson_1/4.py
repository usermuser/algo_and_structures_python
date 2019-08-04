"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""
import random

########### task with integers ###########
randint_low = int(input('Please enter lower limit for integers: '))
randint_up = int(input('Please enter upper for integers: '))
rand_int = round(random.random())

# apply our range
int_result = (rand_int * (randint_up - randint_low)) + randint_low
print(f'Random integer number in range {randint_low} - {randint_up} is: {int_result}')


########## task with floats ##############
randfloat_low = float(input('Please enter lower float limit: '))
randfloat_up = float(input('Please enter upper float limit: '))
rand_float = random.random()

# apply our range
float_result = (rand_float * (randfloat_up - randfloat_low) + randfloat_low)
print(round(float_result, 4))


######### task with symbols ################
low_sym = input('Please enter any character: ')
up_sym = input('Please enter any character: ')
print(low_sym, up_sym)

# get digital representation of characters
low_sym = ord(low_sym)
up_sym = ord(up_sym)

randy = random.random() * (up_sym - low_sym)
result_ord = round(randy + low_sym)
print(f'result_ord: {result_ord}')
print(f'Character in our range is: {chr(result_ord)}')

