# 24. Avalie a expressão abaixo e explique por que o resultado pode ser surpreendente:

# 1 < 2 == True
# Dica: True é igual a 1 em Python (True == 1 resulta em True). 
# O encadeamento 1 < 2 == True é avaliado como 1 < 2 and 2 == True. O que vale 2 == True?

1 < 2 == True 

print(f'\nResultado 1: {1 < 2}')
print(f'Resultado 2: {1 < 2 == True}')
print(f'Resultado 3: {2 == True}\n')

# Resultado 1: True, porque 2 é maior que 1.

# Resultado 2: False, pois o Python separa essa expressão em (1 < 2) and (2 == True).
# Depois, ele verifica as duas partes: a primeira é True. Já a segunda é False, pois True == 1, o que resultaria em 2 == 1, que é False.

# Resultado 3: False, pois True == 1, e 2 == 1 é False.