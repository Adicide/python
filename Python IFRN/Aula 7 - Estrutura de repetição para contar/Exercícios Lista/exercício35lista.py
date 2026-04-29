# 35. Escreva um programa que imprime os primeiros n números da sequência de Fibonacci, onde n é fornecido pelo usuário. USE APENAS WHILE

n  = int(input('Digite um termo n: '))

repetições = 0
a, b = 0, 1

while repetições < n: 
    print(a) 
    a, b = b, a + b 
    repetições += 1 