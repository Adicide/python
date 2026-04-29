# 38. Escreva um programa que lê n números inteiros e exibe o maior e o menor valor lido.

n = int(input('Digite a quantidade de números a serem lidos: '))
repetições = 0
listanums = []

while repetições < n:
    num = int(input('Digite um número: '))
    listanums.append(num)
    repetições += 1

maior_valor = max(listanums)
menor_valor = min(listanums) 
    
print(f'\nMaior valor lido: {maior_valor}')
print(f'Menor valor lido: {menor_valor}')