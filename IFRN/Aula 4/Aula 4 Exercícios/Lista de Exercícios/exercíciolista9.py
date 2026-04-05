# 9. Qual é o resultado da expressão abaixo? 
# Avalie manualmente respeitando a precedência de operadores e depois confirme no interpretador Python.

# not (E and A + 1 < B or D)

A=4
B=10
C=4
D=True
E=False

print(not (E and A + 1 < B or D))

# Resultado: not (False and True or True) => not True => False