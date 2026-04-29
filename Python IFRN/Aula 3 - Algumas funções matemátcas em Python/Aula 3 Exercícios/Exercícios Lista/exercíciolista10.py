# Exercício 10 — Comparando raiz quadrada com arredondamentos (math.sqrt(), math.ceil(), math.floor())
# Escreva um programa que leia um número real positivo, calcule sua raiz quadrada e exiba: 
# o valor exato da raiz, o arredondamento para baixo e o arredondamento para cima.

# Exemplo de entrada e saída:
# Digite um número positivo: 10
# Raiz quadrada de 10.0 : 3.1622776601683795
# Arredondamento para baixo: 3
# Arredondamento para cima: 4

import math

num=float(input('Insira um número real positivo: '))

sqrtnum=math.sqrt(num)
arrencima_sqrt=math.ceil(sqrtnum)
arrenbaixo_sqrt=math.floor(sqrtnum)

print(f'\nA raiz quadrada de {num} é: {sqrtnum}', f'\nArredondamento da raiz para baixo: {arrenbaixo_sqrt}', f'\nArredondamento da raiz para cima: {arrencima_sqrt}')