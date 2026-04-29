# 7. Escreva um programa que recebe um número inteiro positivo n e imprime a soma dos números de 1 a n.

# Exemplo de entrada	Saída esperada
# 5	                        15
# 10	                    55

n = int(input('Digite um número positivo: '))
fator_a = 1 # Fator de adição
soma = 0

# Na parte abaixo, o fator_a está servindo como um medidor de quantas vezes a soma foi feita. 
# Quanto ele se igualar ao valor de n, ele faz a soma uma última vez e o loop para.
while fator_a <= n: 
    soma += fator_a
    fator_a += 1
print(soma)