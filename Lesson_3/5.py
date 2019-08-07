#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

arr = [2, -3, 1, 5, -12, 20, -47, 22, 0]

print(min(arr))    # для проверки

mymin = arr[0]

for i in range(1, len(arr)):
    if arr[i] < mymin:
        mymin = arr[i]

if mymin < 0:
    print(f'The biggest negative nume = {mymin}, and it\'s index = {arr.index(mymin)}')
else:
    print('no negative nums')