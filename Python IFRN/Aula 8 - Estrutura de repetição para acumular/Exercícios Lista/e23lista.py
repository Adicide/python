# Questão 23 — Série harmônica

# Leia um número real X (X > 0). 
# Calcule quantos termos da série harmônica H = 1 + 1/2 + 1/3 + ... + 1/n são necessários para que H supere X. 
# Imprima o número de termos.

# Exemplo:
# Entrada: 2.0
# Saída: 4 (1 + 0.5 + 0.333... + 0.25 = 2.083...)

x = float(input('Digite um número: '))

denominador = 1 # Denominador da série harmônica (H = 1 + 1/2 + 1/3 + ... + 1/n)
divisão = 0  # Divisão = H
lista_divisões = '' 
termos = 0
soma_divisões = 0

while soma_divisões <= x: # Enquanto H não supera X: ...
    divisão = 1 / denominador
    soma_divisões += divisão
    termos += 1
    lista_divisões += f'{divisão:.3f} + '
    denominador += 1
lista_divisões =  lista_divisões[:-3]
print(f'\nQuantidade de termos necessários: {termos} ({lista_divisões} = {soma_divisões:.3f})')