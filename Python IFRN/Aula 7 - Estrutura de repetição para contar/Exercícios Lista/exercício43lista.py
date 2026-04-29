# 43. Escreva um programa que lê números inteiros positivos do usuário 
# enquanto o usuário não digitar um valor negativo, 
# e ao final exibe quantos dos números lidos são pares e quantos são ímpares.

pares = 0
ímpares = 0


while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    
    if n % 2 == 0:
        pares += 1
    else:
        ímpares += 1

print(f'\nQuantidade de números pares: {pares}')
print(f'Quantidade de números ímpares: {ímpares}')