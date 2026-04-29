# 33. Escreva um programa que lê números inteiros 
# enquanto o usuário não digitar 0, e ao final 
# exibe a soma dos números pares e a soma dos números ímpares lidos.

soma_pares = 0
soma_ímpares = 0

while True:
    n = int(input('Digite um número: '))
    
    if n == 0:
        break
    
    if n % 2 == 0:
        soma_pares += n
    else:
        soma_ímpares += n
    
print(f'\nSoma dos números pares: {soma_pares}')
print(f'Soma dos números ímpares: {soma_ímpares}')