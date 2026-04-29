# 32. Escreva um programa que recebe um número inteiro n e exibe todos os divisores de n.

n = int(input('Digite um número: '))
print(f'\nDivisores de {n}:')
divisor = 1
repetições = 0

while repetições < n:
    if n % divisor == 0:
        print(divisor)
    divisor += 1
    repetições += 1