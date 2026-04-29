# 27. Escreva um programa que lê 10 números inteiros 
# e exibe quantos são positivos, quantos são negativos e quantos são iguais a zero.

repetições = 0
positivos = 0
negativos = 0
zeros = 0

while repetições < 10:
    n = int(input('Digite um número: '))
    
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
    else:
        zeros += 1
        
    repetições += 1

print(f'\nQuantidade de números positivos: {positivos}')
print(f'Quantidade de números negativos: {negativos}')
print(f'Quantidade de números iguais a zero: {zeros}')