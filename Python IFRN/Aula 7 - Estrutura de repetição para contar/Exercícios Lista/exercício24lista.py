# 24. Escreva um programa que recebe um número inteiro positivo n 
# e exibe a soma dos dígitos de n.

n = int(input('Digite um número: '))

soma_dígitos = 0
repetições = 0 # Contador

while repetições < len(str(n)):
    soma_dígitos += int(str(n)[repetições])
    repetições += 1
print(f'\nA soma dos dígitos de {n} é: {soma_dígitos}')