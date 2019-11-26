#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

try:
    letter1 = ord(input('Please input any latin letter: '))
    letter2 = ord(input('Please input any latin letter: '))
except:    # don't use bare except!
    print('Please, next time enter latin letters... bye')
    quit()

if letter1 == letter2:
    print('You entered equal letters... bye')
    quit()

ascii_offset = 96
pos1 = letter1 - ascii_offset
pos2 = letter2 - ascii_offset

print(f'positions are: {pos1} and {pos2}')
print(f'beetween them we have {abs(pos2-pos1)} letters')



