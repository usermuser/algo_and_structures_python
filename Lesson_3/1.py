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


# Let's check all numbers in tuple t
for i in t:
    if checker(i,myrange):
        c += 1

print(f'So, {c} numbers are multiple of each number in range 2 to 9')

