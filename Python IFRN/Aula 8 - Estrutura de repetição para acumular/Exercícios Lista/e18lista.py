# Questão 18 — Mínimo múltiplo comum (MMC)

# Leia dois inteiros positivos A e B. Calcule e imprima o MMC de A e B usando while (sem usar a fórmula direta com MDC).

# Exemplo:

# Entrada: 4 6
# Saída: 12

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

mmc = max(a, b)

while mmc % a != 0 or mmc % b != 0:
    mmc += 1
print(f'\nMMC({a}, {b}) = {mmc}')