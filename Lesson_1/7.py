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

l1 = 3
l2 = 4
l3 = 2

maxl = max(l1, l2, l3)

if l1 == l2 == l3:
    print('Это равносторонний треугольник')

if l1 == l2 or l1 == l3 or l2 == l3:
    print('Это равнобедренный треугольник')

