# 8. Escreva um programa que recebe um número inteiro positivo n e imprime o produto (fatorial) de 1 × 2 × ... × n.

# Exemplo de entrada	Saída esperada
# 4	                        24
# 5	                        120

n = int(input('Digite um número positivo: '))
fator_m = 1 # Fator de multiplicação
m = 1 # Multiplicação

# Abaio, o fator_m determina quantas multiplicações foram feitas. 
# Quando ele for igual a n, ele faz a última operação e, depois, o loop para.
while fator_m <= n: 
    m *= fator_m
    fator_m += 1
print(m)