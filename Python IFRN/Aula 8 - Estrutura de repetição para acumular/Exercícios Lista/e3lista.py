# Questão 3 — Tabuada

# Leia um número inteiro N (1 ≤ N ≤ 10). Imprima a tabuada de multiplicação de N, do 1 ao 10, no formato N x i = resultado.

# Exemplo (N=3):
# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 10 = 30

n = int(input('Digite um número: '))
print(f'\nTabuada do {n}:')

repetição = 0
fator_m = 0 # Fator da multiplicação
while repetição < 10:
    fator_m += 1
    multiplicação = n * fator_m
    print(f'{n} * {fator_m} = {multiplicação}')
    repetição += 1