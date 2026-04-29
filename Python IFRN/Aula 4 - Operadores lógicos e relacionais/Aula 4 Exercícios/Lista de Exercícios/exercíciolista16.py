# 16. A expressão abaixo tem resultado diferente da expressão da questão anterior? 
# Avalie e explique o que muda com o uso dos parênteses.
 
# A == C and (B > A or not E)

A=4
B=10
C=4
E=False

print(A==C and (B > A or not E))

# Resultado: True and (True or True) => True and True => True. Logo, o resultado não se altera.
# O que muda com o uso dos parênteses é que o computador irá priorizar o que está dentro dele, assim como em uma operação matemática.
# Depois, ele vai comparar com a expressão 'A==C' e dará o resultado.