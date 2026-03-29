# 1. Escreva um programa que tem como entrada 3 números reais e imprime o menor destes números.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

minnums = min(num1, num2, num3)

print(f'\nO menor número é: {minnums}')