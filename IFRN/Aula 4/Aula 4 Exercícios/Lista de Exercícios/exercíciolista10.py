# 10. Usando operadores lógicos e relacionais, escreva uma expressão em Python que resulte em 
# True somente quando A for um número par e estiver entre 1 e 9 (inclusive). 
# Use o açúcar sintático de encadeamento na parte da comparação de intervalo.

# Dica: um número é par quando o resto da divisão por 2 é igual a zero (A % 2 == 0).

A=4

if 1<=A<=9 and A%2==0:
    print(True)

# Resultado: True