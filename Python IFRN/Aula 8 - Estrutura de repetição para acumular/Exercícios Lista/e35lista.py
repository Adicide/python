# Questão 35 — Maior primo fator

# Leia um inteiro positivo N (N ≥ 2). Encontre e imprima o maior fator primo de N.

# Exemplo:
# Entrada: 84
# Saída: 7 (84 = 2² × 3 × 7)

n = int(input('Digite um número: '))
n_original = n

maior_fator = 1
divisor = 2 

while divisor * divisor <= n:
    while n % divisor == 0:
        maior_fator = divisor
        n //= divisor
    divisor += 1
    
if n > 1:
    maior_fator = n
print(f'\nMaior fator de {n_original}: {maior_fator}')  