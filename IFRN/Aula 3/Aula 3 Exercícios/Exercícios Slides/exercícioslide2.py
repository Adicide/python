# 2. Escreva um programa que tem como entrada um número real positivo e maior do que zero e que calcula e imprime: (a) o quadrado do número; (b) a raiz quadrada do número; (c) a raiz cúbica do número.

import math

num = float(input('Digite um número maior do que zero: '))

a=num**2
b=math.sqrt(num)
c=math.cbrt(num)

print(f'\nO quadrado desse número é: {a}')
print(f'A raiz quadrada desse número é: {b}')
print(f'A raiz cúbica desse número é: {c}')