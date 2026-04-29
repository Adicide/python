# 40. Escreva um programa que recebe um inteiro positivo n e determina se n é um número perfeito 
# (um número é perfeito se a soma de seus divisores próprios (excluindo ele mesmo) é igual a ele mesmo, ex: 6 = 1+2+3).

n = int(input('Digite um número: '))

lista_divisores = [] # Lista dos divisores 
divisor = 0 # Verifica se um número é divisor de n
repetição = 0 # Contador
soma_divisores = 0
posição_divisor = 0

while repetição < n:
    divisor += 1
    
    if n % divisor == 0:
        if divisor < n:
            lista_divisores.append(divisor)
            soma_divisores += lista_divisores[posição_divisor]
            posição_divisor += 1

    repetição += 1

if soma_divisores == n:
    print(f'\n{n} é um número perfeito.')
else:
    print(f'\n{n} não é um número perfeito.')