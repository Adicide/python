# 25. Combine tudo que aprendeu e escreva uma única expressão que resulte em True 
# somente quando todas as condições abaixo forem verdadeiras ao mesmo tempo:

# A é par
# B é maior que o dobro de A
# G está no intervalo [-5, -1] (inclusive)
# D é verdadeiro

# Use o açúcar sintático de encadeamento para a verificação do intervalo de G e organize a expressão de forma legível.

A=4
B=10
D=True
G=-3

print(A % 2 == 0 and B > 2 * A and D == True and -5 <= G <= -1)

# Resultado: True and True and True and True => True