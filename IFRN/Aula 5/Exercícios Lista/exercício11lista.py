# 11. Leia um número inteiro. Se ele for divisível tanto por 2 quanto por 3, exiba "Divisível por 2 e por 3".

num=int(input('\nDigite um número inteiro: '))

if num % 2 == 0 and num % 3 == 0:
    print('Divisível por 2 e por 3.\n')