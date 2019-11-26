#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

letter1 = input('Please input any latin letter: ')
letter2 = input('Please input any latin letter: ')

# to get position of letter we need to convert it to ascii code and substitute the offset
ascii_offset = 96
pos1 = ord(letter1) - ascii_offset
pos2 = ord(letter2) - ascii_offset

print(f'position of \'{letter1}\' is {pos1} and position of \'{letter2}\' is {pos2}')

if pos2 > pos1:
    print(f'between them we see {pos2 - pos1} other letters')
else:
    print(f'between them we have {pos1 - pos2} other letters')


