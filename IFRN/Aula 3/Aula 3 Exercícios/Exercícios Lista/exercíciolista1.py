# Exercício 1 — Menor entre três números (min())
# Escreva um programa que leia três números reais digitados pelo usuário e imprima o menor deles.

# Exemplo de entrada e saída:
# Digite o primeiro número: 7.5
# Digite o segundo número: 3.2
# Digite o terceiro número: 9.0
# O menor número é: 3.2

num1 = float(input('Digite o 1° número: '))
num2 = float(input('Digite o 2° número: '))
num3 = float(input('Digite o 3° número: '))

menornum=min(num1,num2,num3)

print(f'\nO menor número é: {menornum}')