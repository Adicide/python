# Questão 12 — Inversão de número

# Leia um número inteiro positivo N. Imprima o número com seus dígitos na ordem inversa.

# Exemplo:
# Entrada: 1234
# Saída: 4321

n = int(input('Digite um número: '))

repetição = 0
inverso = ''
while repetição < len(str(n)):
    inverso += str(n)[len(str(n)) - 1 - repetição]
    repetição += 1
print(f'\nInverso de {n}: {inverso}')