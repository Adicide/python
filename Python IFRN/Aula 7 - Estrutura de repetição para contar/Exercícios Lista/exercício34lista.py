# 34. Escreva um programa que recebe dois inteiros positivos a e b 
# e calcula o Máximo Divisor Comum (MDC) usando o algoritmo de Euclides com while. 

# Como Funciona (Passo a Passo)

# Divida o maior número (a) pelo menor (b), obtendo um quociente (q) e um resto (r): a = b * q + r
# Substitua: O divisor (b) torna-se o novo dividendo, e o resto (r) torna-se o novo divisor.
# Repita o processo até que o resto seja 0.

# Resultado: O último divisor (o resto diferente de zero antes de chegar a zero) é o MDC. 

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

r = 0

while b != 0:
    r = a % b 
    a = b 
    b = r 
print(f'\nMDC: {a}')