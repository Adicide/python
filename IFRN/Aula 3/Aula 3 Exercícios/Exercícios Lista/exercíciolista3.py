# Exercício 3 — Raiz quadrada de um número (math.sqrt())
# Escreva um programa que leia um número real positivo digitado pelo usuário e imprima a sua raiz quadrada.

# Exemplo de entrada e saída:
# Digite um número positivo: 25
# A raiz quadrada de 25.0 é: 5.0

import math

num=float(input('Digite qualquer número positivo: '))
numsqrt=math.sqrt(num)

print(f'\nA raiz quadrada de {num} é: {numsqrt}')