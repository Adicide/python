# 3. Escreva um programa que tem como entrada cinco números inteiros, ignora
# o menor número e o maior número, e que calcula a média aritmética dos três
# número restantes.

import math

num1=int(input('Digite o primeiro número: '))
num2=int(input('Digite o segundo número: '))
num3=int(input('Digite o terceiro número: '))
num4=int(input('Digite o quarto número: '))
num5=int(input('Digite o quinto número: '))

menornum=min(num1,num2,num3,num4,num5)
maiornum=max(num1,num2,num3,num4,num5)

somanums=(num1+num2+num3+num4+num5)-maiornum-menornum
médianums=somanums/3

print(f'\nA média dos números, excluindo o maior e o menor, é: {médianums}')