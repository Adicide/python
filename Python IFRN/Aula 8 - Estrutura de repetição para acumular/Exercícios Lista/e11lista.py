# Questão 11 — Soma dos dígitos

# Leia um número inteiro positivo N. Calcule e imprima a soma dos dígitos que compõem N.

# Exemplo:
# Entrada: 1234
# Saída: 10

n = input('Digite um número: ')

repetição = 0
soma = 0

while repetição < len(n):
    soma += int(n[repetição])
    repetição += 1
print(f'\nSoma dos dígitos de {n}: {soma}')