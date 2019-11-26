# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.

x1 = int(input('Please, type X coordinate for first point: '))
y1 = int(input('Please, enter Y coordinate for first point: '))
x2 = int(input('Please, enter X coordinate for second point: '))
y2 = int(input('Please, enter Y coordinate for second point: '))

k = (y2-y1) / (x2-x1)
b = y2 - k*x2

print(f'Уравнения прямой для этих точек = y = {k}x+{b}')



