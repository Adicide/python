# 6. Escreva um programa que recebe um número inteiro positivo n como entrada e imprime todos os inteiros de 1 a n.

# Exemplo de entrada	Saída esperada
#                             1
# 4	                          2
#                             3
#                             4

#                             1
#                             2
#                             3
# 7	                          4
#                             5
#                             6
#                             7

n = int(input('Digite um número: '))
x = 0 

while x < n:
    x += 1
    print(x)