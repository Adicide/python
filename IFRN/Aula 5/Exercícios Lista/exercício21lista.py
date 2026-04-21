# 21. Leia um número inteiro. 
# Se ele for divisível por 7, exiba "Divisível por 7"; caso contrário, exiba "Não divisível por 7".

num = int(input('Insira um número: '))

if num % 7 == 0:
    print(f'\nO número {num} é Divisível por 7.')
else:
    print(f'\nO número {num} Não é divisível por 7.')