# 48. Escreva um programa que recebe um inteiro positivo n e verifica se ele é um palíndromo numérico (lê-se igual de trás para frente).

n = int(input('Digite um número: '))
repetição = 0
posição = ''

while repetição < len(str(n)):
    posição += str(n)[len(str(n)) - 1 - repetição]
    repetição += 1
    
if int(posição) == n:
    print(f'\n{n} é um palíndromo.')
else:
    print(f'\n{n} não é um palíndromo.')