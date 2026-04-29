# 42. Escreva um programa que recebe um inteiro positivo n 
# e exibe todos os números no intervalo [1, n] que são simultaneamente divisíveis por 2 e por 7.

n = int(input('Digite um número: '))
repetição = 0

while repetição < n:
    repetição += 1
    if repetição % 2 == 0 and repetição % 7 == 0:
        print(repetição)