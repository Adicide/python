# 21. Em Python, os operadores and e or não retornam necessariamente True ou False — eles retornam um dos próprios operandos. 
# Avalie cada expressão abaixo e explique por que o resultado é o que é:

# A and B
# E and A
# D or B
# E or A

A=4
B=10
D=True
E=False

print(f'\nResultado 1: {A and B}')
print(f'Resultado 2: {E and A}')
print(f'Resultado 3: {D or B}')
print(f'Resultado 4: {E or A}\n')

# Resultado 1: 10, pois o operando A é verdadeiro, permitindo que o operador lógico 'and' retorne o 2° operando (10).

# Resultado 2: False, pois o operador lógico 'and' retorna o primeiro valor falso que encontra. Se o primeiro valor ou todos fossem verdadeiros,
# ele retornaria o último.

# Resultado 3: True, pois o operador lógico 'or' retorna o primeiro valor verdadeiro que encontra. Se o primeiro valor ou todos fossem falsos,
# ele retornario o último.

# Resultado 4: 4, pois o operando E é falso, permitindo que o operador lógico 'or' retorne o 2° operando (4).