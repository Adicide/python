# 26. Leia um número inteiro. Se o número for maior que 0, exiba seu quadrado; caso contrário, exiba seu cubo.

num = int(input('Digite um número: '))

if num > 0:
    quadrado = num ** 2
    print(f'\nO quadrado de {num} é: {quadrado}')
else:
    cubo = num ** 3
    print(f'\nO cubo de {num} é: {cubo}')