# 49. Escreva um programa que lê n valores inteiros e exibe, ao final:

# a soma total,
# a média,
# o maior valor,
# o menor valor,
# a quantidade de valores acima da média.

n = int(input('Digite a quantidade de números a serem lidos: '))
print('')
repetição = 0  

listanums = []
soma_total = 0
acima_média = 0 # Valores acima da média

# Primeiro loop (para adicionar os números à lista e calcular a soma)
while repetição < n:
    num = int(input('Digite um número: '))
    listanums.append(num)
    soma_total += num
    repetição += 1

# Segundo loop (para calcular valores acima da média)
repetição = 0 
média = soma_total / n
while repetição < n:
    if listanums[repetição] > média:
        acima_média += 1
    repetição += 1
    
print(f'\nSoma total: {soma_total}')
print(f'Maior valor: {max(listanums)}')
print(f'Menor valor: {min(listanums)}')
print(f'Quantidade de valores acima da média ({média:.2f}): {acima_média}')