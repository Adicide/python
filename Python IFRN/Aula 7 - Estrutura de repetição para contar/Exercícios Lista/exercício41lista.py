# 41. Escreva um programa que lê n pares de números inteiros (a, b)
# e, para cada par, informa qual é o maior, qual é o menor, ou se são iguais.

n = int(input('Digite a quantidade de pares a serem lidos: '))

repetição = 0

while repetição < n:
    a = int(input('\nDigite o primeiro número do par: '))
    b = int(input('Digite o segundo número do par: '))
    
    if a > b:
        maior = a
        menor = b
        print(f'\nMaior = {maior}')
        print(f'Menor = {menor}')
    elif b > a:
        maior = b
        menor = a
        print(f'\nMaior = {maior}')
        print(f'Menor = {menor}')
    elif a == b:
        print(f'\nOs números são iguais.')
        
    repetição += 1