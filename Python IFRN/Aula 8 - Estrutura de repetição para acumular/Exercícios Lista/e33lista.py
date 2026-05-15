# Questão 33 — Sequência de Padovan

# A sequência de Padovan é definida por: P(0)=P(1)=P(2)=1 e P(n) = P(n-2) + P(n-3).
# Leia N e imprima os N primeiros termos.

# Exemplo (N=8):
# Saída: 1 1 1 2 2 3 4 5

n = int(input('Digite um número: '))
p0 = 1
p1 = 1
p2 = 1
termos = 0 

while termos < n:
    print(p0)
    pn = p1 + p0
    p0 = p1
    p1 = p2
    p2 = pn
    termos += 1