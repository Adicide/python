# 11. Escreva um programa que recebe um número inteiro positivo n e imprime a tabuada de multiplicação de n (de 1 a 10).

# Exemplo de entrada	Saída esperada
# 	                    3 x 1 = 3
# 3                     3 x 2 = 6
#                           ...
#                       3 x 10 = 30

n = int(input('Digite um número: '))
print(f'\nTabuada do {n}')
contador_m = 0 # Fator de multiplicação

while contador_m < 10:
    contador_m += 1
    resultado = n * contador_m
    print(f'{n} * {contador_m} = {resultado}')