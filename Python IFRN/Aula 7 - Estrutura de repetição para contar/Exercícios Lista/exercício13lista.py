# 13. Escreva um programa que recebe um número inteiro positivo n e imprime os múltiplos de 3 entre 1 e n.

# Exemplo de entrada	Saída esperada
#   	                        3
# 10                            6 
#                               9

# 	                            3
#                               6
# 15                            9
#                               12
#                               15

num = int(input('Digite um número positivo: '))
contador_num = 0 # Contador

while contador_num <= num:
    contador_num += 1
    if contador_num % 3 == 0:
        print(contador_num)