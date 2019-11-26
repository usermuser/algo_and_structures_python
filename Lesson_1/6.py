# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

num = int(input('Please enter a number: '))
ascii_num = num + ord('a') - 1
print(f'Corresponding letter for this number is \'{chr(ascii_num)}\'')