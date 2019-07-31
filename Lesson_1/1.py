# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
user_input = int(input('Please type three-digit number: '))

first_digit = user_input // 100
second_digit = (user_input // 10) % 10
third_digit = user_input % 10

print(f'Sum of numbers: {first_digit + second_digit + third_digit}')
print(f'Result of multiplication of numbers: {first_digit * second_digit * third_digit}')