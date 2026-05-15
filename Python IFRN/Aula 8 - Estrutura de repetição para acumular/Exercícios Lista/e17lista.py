# Questão 17 — Máximo divisor comum (MDC)

# Leia dois inteiros positivos A e B. Use o algoritmo de Euclides com while para calcular e imprimir o MDC de A e B.

# Exemplo:

# Entrada: 48 18
# Saída: 6

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
a_original = a 
b_original = b

while b != 0:
    r = a % b
    a = b
    b = r
    
print(f'\nMDC({a_original}, {b_original}) = {a}')