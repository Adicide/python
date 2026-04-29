# 37. Escreva um programa que recebe um inteiro positivo n e exibe o número de dígitos de n.

n = int(input('Digite um número: '))

while n < 0:
    print('\nNúmero negativo não vale. Apenas positivos.')
    n = int(input('Digite um número: '))

print(f'\nQuantidade de dígitos de {n} é: {len(str(n))}')