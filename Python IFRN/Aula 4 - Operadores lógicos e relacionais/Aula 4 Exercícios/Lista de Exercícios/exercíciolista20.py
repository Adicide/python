# 20. Escreva uma expressão Python que resulte em True 
# somente quando todas as condições abaixo forem satisfeitas ao mesmo tempo:

# A é maior que C ou B é igual a 10
# G é negativo
# E é False

A = 4
B = 10
C = 4
D = True
E = False
G = -3

print(f'\nExpressão 1: {A > C or B == 10 and G < 0 and E == False}')

# OU

if A>C or B==10 and G<0 and E==False:
    print(f'Expressão 2: {True}\n')

# Resultado: False or True and True and True => False or True => True (ambas as expressões)