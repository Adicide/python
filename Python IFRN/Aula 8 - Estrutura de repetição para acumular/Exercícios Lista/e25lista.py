# Questão 25 — Sequência até superar limite

# Considere a sequência definida por: a(1) = 1, a(n) = a(n-1) + 2*n - 1. 
# Leia um inteiro L. Encontre o menor n tal que a(n) > L. 
# Imprima n e a(n).

# Exemplo (L=20):
# Saída: n=5, a(5)=25

l = int(input('Digite um número: '))
n = 1
a = 1

while a < l:
    n += 1
    a = a + 2*n - 1
print(f'\nn = {n}, a({n}) = {a}')