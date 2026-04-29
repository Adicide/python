# 20. Escreva um programa que calcula
# e exibe a soma: 1 + 1/2 + 1/3 + 1/4 + ... + 1/n, onde n é fornecido pelo usuário. USE SOMENTE WHILE

n = int(input('Digite um número: '))

soma = 0
denominador = 1

while denominador <= n:
    soma += 1/denominador
    denominador += 1

print(soma)