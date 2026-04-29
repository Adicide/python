# 22. Usando F = 0, avalie as expressões abaixo e explique o comportamento (curto-circuito e valor retornado):

# F or A
# F and A

A=4
F=0

print(f'\nResultado 1: {F or A}')
print(f'Resultado 2: {F and A}\n')

# Resultado 1: 4, pois o operador lógico 'or' retorna o primeiro valor verdadeiro encontrado. 
# Nesse caso, ele encontrou um valor falso, o que faz com que ele retorne o valor A (4).

# Resultado 2: 0, pois o operador lógico 'and' retorna o primeiro valor falso encontrado. Caso contrário, retornaria 4.
# Como F = 0 e 0 é um valor falso (falsy), ele acaba retornando-o.