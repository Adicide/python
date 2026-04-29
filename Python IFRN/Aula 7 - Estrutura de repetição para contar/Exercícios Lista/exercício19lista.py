# 19. Escreva um programa que imprime os primeiros n termos da progressão aritmética 
# com primeiro termo a e razão r, onde n, a e r são fornecidos pelo usuário.

# an = a1 + (n - 1)r

a1 = int(input('Digite o 1° termo: ')) # Contador
n = int(input('Ótimo. Agora, digite o termo n: '))
r = int(input('Insira a razão: '))

while a1 <= n:
    print(a1)
    a1 += r