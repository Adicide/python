# Exercício 6 — Menor e maior entre cinco números (min() e max())
# Escreva um programa que leia cinco números inteiros digitados pelo usuário e imprima o menor e o maior deles.

# Exemplo de entrada e saída:
# Digite o 1º número: 10
# Digite o 2º número: 3
# Digite o 3º número: 7
# Digite o 4º número: 15
# Digite o 5º número: 1
# O menor número é: 1
# O maior número é: 15

import math

num1=int(input('Insira o 1° número: '))
num2=int(input('Insira o 2° número: '))
num3=int(input('Insira o 3° número: '))
num4=int(input('Insira o 4° número: '))
num5=int(input('Insira o 5° número: '))

mennum=min(num1,num2,num3,num4,num5)
mainum=max(num1,num2,num3,num4,num5)

print(f'\nO menor número é: {mennum}')
print(f'O maior número é: {mainum}')