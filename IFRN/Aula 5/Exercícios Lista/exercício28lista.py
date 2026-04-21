# 28. Leia dois números inteiros. Se a soma deles for maior que 100, exiba "Soma grande"; caso contrário, exiba "Soma pequena".

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = num1 + num2

if soma > 100:
    print('\nSoma grande')
else:
    print('\nSoma pequena')