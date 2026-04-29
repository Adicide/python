# 23. O padrão x and y or z era usado antigamente em Python como uma alternativa ao operador ternário y if x else z. 
# Avalie a expressão abaixo com D = True e depois com D = False, e explique o que cada caso retorna:

# D and B or A
# Observação: hoje a forma recomendada é B if D else A. Teste ambas e compare os resultados.

A = 4
B = 10
D = True

print(f'\nResultado 1: {D and B or A}')

D = False

print(f'Resultado 2: {B if D else A}\n')

# Resultado 1: 10, pois 'D' é um valor verdadeiro, forçando o programa a retornar 'B'.

# Resultado 2: 4, porque 'D' é um valor falso, fazendo com que o programa esqueça 'B' e retorne 'A'.
# Ele só retornaria 'B' se 'D' fosse verdadeiro.