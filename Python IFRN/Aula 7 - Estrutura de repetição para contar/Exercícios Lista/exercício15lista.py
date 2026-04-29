# 15. Escreva um programa que lê números inteiros do usuário enquanto o usuário não digitar 0, e ao final 
# exibe a quantidade de números lidos (sem contar o zero).

num = int(input('Digite um número: '))
contador = 0 # Quantidade de números

while num != 0:
    num = int(input('Digite um número: '))
    contador += 1

print('\nOperação terminada.')
print(f'Total de números lidos: {contador}')