# # Questão 30 — Critério de Gauss: soma de PA

# Em uma progressão aritmética (PA), a soma dos N primeiros termos é S = N*(a1 + aN)/2. 
# Leia os valores a1 (primeiro termo), r (razão) e S_max (soma máxima desejada). 
# Usando while, some os termos da PA um a um até que a soma ultrapasse S_max ou atinja 1000 termos. 
# Imprima quantos termos foram somados e a soma final.

a1 = int(input('Digite o primeiro termo (a1): ')) # a1 ou Primeiro Termo
r = int(input('Digite a razão: ')) # Razão 
soma_max = int(input('Insira a soma máxima: '))

soma = 0 
termos = 0
an = a1

while soma <= soma_max and termos < 1000:
    soma += an
    termos += 1
    an += r # Próximo termo será a soma do atual com a razão.

print(f'\nQuantidade de termos somados: {termos}')
print(f'Soma final: {soma}')