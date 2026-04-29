# 23. Escreva um programa que imprime os quadrados perfeitos 
# menores ou iguais a 100 (ou seja, 1, 4, 9, 16, ..., 100).

repetições = 0
base = 0

while repetições < 10:
    base += 1
    quadrado_base = base ** 2
    print(quadrado_base)
    repetições += 1