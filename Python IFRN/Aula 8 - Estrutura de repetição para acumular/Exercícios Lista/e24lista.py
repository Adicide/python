# Questão 24 — Raiz inteira

# Leia um inteiro não-negativo N. Sem usar funções de raiz quadrada, encontre o maior inteiro k tal que k² ≤ N. Imprima k.

# Exemplo:

# Entrada: 26
# Saída: 5 (5² = 25 ≤ 26 < 36 = 6²)

n = int(input('Digite um número: '))

k = 0
while k ** 2 <= n:
    k += 1
print(k - 1)