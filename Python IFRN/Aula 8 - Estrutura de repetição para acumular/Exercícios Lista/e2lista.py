# Questão 2 — Soma dos primeiros N inteiros

# Leia um número inteiro positivo N. Calcule e imprima a soma de todos os inteiros de 1 até N.

# Exemplo:
# Entrada: 10
# Saída: 55

n = int(input('Digite um número: '))

repetição = 0
soma = 0
while repetição < n:
    repetição += 1
    soma += repetição
print(f'\nSoma total: {soma}')