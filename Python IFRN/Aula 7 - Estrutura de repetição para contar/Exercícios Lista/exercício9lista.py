# 9. Escreva um programa que lê 5 números inteiros digitados pelo usuário e imprime a soma deles.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
num4 = int(input('Digite o quarto número: '))
num5 = int(input('Digite o quinto número: '))

a = 0 # Fator de soma
listanum = [num1, num2, num3, num4, num5]
soma = 0

while a <= max(listanum):
    soma += a
    a += 1
print(f'\nA soma dos números é: {soma}')