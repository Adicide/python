# 16. Leia um número inteiro. Se ele for par, exiba "Par"; caso contrário, exiba "Ímpar".

num = int(input('Insira um número: '))

if num % 2 == 0:
    print(f'\nO número {num} é Par.')
else:
    print(f'\nO número {num} é Ímpar.')