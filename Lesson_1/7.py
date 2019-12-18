"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""

"""
Примечания ко всем задачам урока:
1.	Решите задачу при помощи линейного алгоритма или алгоритма с ветвлением 
(цикл и рекурсии будут на уроке 2 и тут их не используем для решения).
2.	Аналогично п. 1. массивы пройдём на уроке 3, поэтому постарайтесь решить задачи без них.
3.	Если речь идёт о символах, используйте только строчные буквы английского алфавита.
"""

# Неравенство треугольника: длина каждого отрезка меньше суммы длин двух других отрезков
# Если все отрезки равны, то это равносторонний треугольник
# Если две стороны равны, то это равнобедренный треугольник

try:
    l1 = int(input('Введите длину первого отрезка: '))
    l2 = int(input('Введите длину второго отрезка: '))
    l3 = int(input('Введите длину третьего отрезка: '))

    if l1 >= l2 + l3 or l2 >= l1 + l3 or l3 >= l2 + l1:
        print('Это не треугольник')
    elif l1 == l2 == l3:
        print('Это равносторонний треугольник')
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print('Это разносторонний треугольник')
    else:
        print('Равнобедренный')
except:     # don't use bare except, I know, I know...
    print('Данные не корректны')