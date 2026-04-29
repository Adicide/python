# 16. Escreva um programa que lê números reais do usuário enquanto o usuário 
# não digitar um número negativo, e ao final exibe a soma de todos os valores lidos (sem incluir o negativo).

num = float(input('Digite um número: '))
quantidade_nums = 0 # Contador

while num >= 0:
    num = float(input('Digite um número: '))
    quantidade_nums += 1
    
print('\nOperação terminada.')
print(f'Total de números lidos: {quantidade_nums}')