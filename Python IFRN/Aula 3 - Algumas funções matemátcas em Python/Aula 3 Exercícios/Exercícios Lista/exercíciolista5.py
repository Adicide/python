# Exercício 5 — Arredondamento para baixo (math.floor())
# Escreva um programa que leia um número real digitado pelo usuário 
# e imprima o maior número inteiro menor ou igual a ele (arredondamento para baixo).

# Exemplo de entrada e saída:
# Digite um número real: 4.7
# O arredondamento para baixo de 4.7 é: 4

import math

num=float(input('Insira um número real: '))
num_arren=math.floor(num)

print(f'\nO arredondamento para baixo de {num} é: {num_arren}')