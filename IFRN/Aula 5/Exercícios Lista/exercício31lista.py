# 31. Leia um número inteiro. Se for positivo, exiba "Positivo"; 
# se for negativo, exiba "Negativo"; 
# se for zero, exiba "Zero".

num = int(input('Digite um número: '))

if num > 0:
    print(f'\n{num} é Positivo.')
elif num == 0:
    print(f'\n{num} é Zero.')
else:
    print(f'\n{num} é Negativo.')