# 26. Escreva um programa que imprime os números de 1 a 20 
# e, ao lado de cada número, escreve "par" se o número for par ou "ímpar" se for ímpar.

n = 0 

while n < 20:
    n += 1
    if n % 2 == 0:
        print(str(n) + ' Par')
    elif n % 2 != 0:
        print(str(n) + ' Ímpar')