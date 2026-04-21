# 15. Leia um número inteiro. Se ele for múltiplo de 5, exiba "Múltiplo de 5".

num = int(input('Digite um número: '))

if num % 5 == 0:
    print(f'\n{num} é múltiplo de 5.')
else:
    print(f'\n{num} não é múltiplo de 5.')