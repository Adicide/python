# Exercício 2 — Maior entre três números (max())
# Escreva um programa que leia três números reais digitados pelo usuário e imprima o maior deles.

# Exemplo de entrada e saída:
# Digite o primeiro número: 7.5
# Digite o segundo número: 3.2
# Digite o terceiro número: 9.0
# O maior número é: 9.0

num1=float(input('Digite o 1° número: '))
num2=float(input('Digite o 2° número: '))
num3=float(input('Digite o 3° número: '))

maiornum=max(num1,num2,num3)

print(f'\nO maior número é: {maiornum}')