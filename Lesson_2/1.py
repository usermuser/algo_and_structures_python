"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""


def add(num1, num2):
    return f'{num1} + {num2} = {num1 + num2}'


def substract(num1, num2):
    return f'{num1} - {num2} = {num1 - num2}'


def mul(num1, num2):
    return f'{num1} * {num2} = {num1 * num2}'


def divide(num1, num2):
    if num2 == 0.0:
        return '[Error] You can\'t divide by zero!'
    else:
        return f'{num1} / {num2} = {num1 / num2}'


def check_op(op):                   # operator validation
    if op not in '+-*/':
        print('wrong operator')


EXIT = False

while not EXIT:
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    op = input('Enter an operator: ')     # operation 0 + - * /

    # check EXIT flag
    if op == '0':
        print('Goodbye my Friend')
        EXIT = True
    else:
        check_op(op)                        # check that operator is correct

        if op == '+':
            print(add(num1, num2))
        elif op == '-':
            print(substract(num1, num2))
        elif op == '*':
            print(mul(num1, num2))
        elif op == '/':
            print(divide(num1, num2))





