# Exercício 4 — Arredondamento para cima (math.ceil())
# Escreva um programa que leia um número real digitado pelo usuário e 
# imprima o menor número inteiro maior ou igual a ele (arredondamento para cima).

# Exemplo de entrada e saída:
# Digite um número real: 4.3
# O arredondamento para cima de 4.3 é: 5

import math

num=float(input('Insira um número real: '))
num_arren=math.ceil(num)

print(f'\nO arredondamento para cima de {num} é: {num_arren}')