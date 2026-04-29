# 47. Escreva um programa que simula um jogo de adivinhação: 
# o programa sorteia um número inteiro entre 1 e 100 e o usuário tenta adivinhar. 
# A cada tentativa o programa informa se o chute foi "muito baixo", "muito alto" ou "acertou!". 
# O laço termina quando o usuário acertar.

# Dica: use import random e random.randint(1, 100) para sortear o número.

import random
número = random.randint(1, 100)

while True:
    tentativa = int(input('Adivinhe qual número de 1 a 100 estou pensando: ')) # Número que o usuário coloca para adivinhar
    
    if tentativa < número:
        print('Muito baixo.\n')
    elif tentativa > número:
        print('Muito alto.\n')
    elif tentativa == número:
        print('Você acertou!')
        break