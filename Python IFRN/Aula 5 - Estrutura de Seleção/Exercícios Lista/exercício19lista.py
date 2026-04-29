# 19. Leia um número real. Se ele for positivo ou zero, exiba "Não negativo"; caso contrário, exiba "Negativo".

num = float(input('Digite um número: '))

if num >= 0:
    print(f'\nO número {num} é Não negativo.')
else:
    print(f'\nO número {num} é Negativo.')