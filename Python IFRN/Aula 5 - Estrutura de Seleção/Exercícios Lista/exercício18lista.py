#  18. Leia dois números inteiros. Exiba o maior deles. Se forem iguais, exiba "Os números são iguais".

import math

num1 = int(input('Digite um número: '))
num2 = int(input('Ótimo. Digite outro número: '))

listanum = [num1, num2]

if num1 != num2:
    print(f'\nO maior número é: {max(listanum)}')
elif num1 == num2:
    print('\nOs números são iguais.')