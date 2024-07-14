from art import logo
flag = True


def add(n1, n2):
  return n1 + n2


def substract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 - n2


def divide(n1, n2):
  return n1 / n2


operations = {'+': add, '-': substract, '*': multiply, '/': divide}

print(logo)
num1 = float(input('Type the first number: '))
for _ in operations:
  total = print(_)
operation_symbol = input('What operation you want to choose: ')
num2 = float(input('Type the second number:'))

function = operations[operation_symbol]
answer = function(num1, num2)

print(f'{num1} {operation_symbol} {num2} = {answer}')

while flag:
  y_n = input('Do you want to exit the program? ').lower()
  if y_n == 'yes':
    flag = False
    exit('Exit')
  elif y_n == 'no':
    flag = True
    operation_symbol = input('What operation you want to choose: ')
    num3 = float(input('What is the second number: '))
    function = operations[operation_symbol]
    second_answer = function(answer, num3)
    print(f'{answer} {operation_symbol} {num3} = {second_answer} ')
    answer = second_answer
    second_answer = num3