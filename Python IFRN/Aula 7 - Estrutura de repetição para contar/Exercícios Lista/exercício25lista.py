# 25. Escreva um programa que recebe um número inteiro positivo n e exibe n na ordem inversa dos dígitos.

n = int(input('Digite um número: '))

inverso = ''
repetições = 0

while repetições < len(str(n)):
    inverso += str(n)[len(str(n)) - 1 - repetições]
    repetições += 1
print(f'\nO inverso de {n} é: {inverso}')