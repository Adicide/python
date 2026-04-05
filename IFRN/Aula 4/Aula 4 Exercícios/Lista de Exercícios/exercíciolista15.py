# 15. Qual é o resultado da expressão abaixo? Identifique a ordem de avaliação respeitando a precedência dos operadores.

# A == C and B > A or not E

A = 4
B = 10
C = 4
E = False

print(A == C and B > A or not E)

# Resultado: A == C and B > A or not E => True and True or True => True or True = True