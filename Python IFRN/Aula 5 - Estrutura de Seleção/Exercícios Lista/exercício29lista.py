# 29. Leia o peso e a altura de uma pessoa e calcule o IMC (peso / altura²). 
# Se o IMC for menor que 25, exiba "Peso normal"; caso contrário, exiba "Acima do peso".

print('*** CALCULADORA DE IMC ***')
peso = float(input('Insira seu peso (ex: 70kg): '))
altura = float(input('Insira sua altura (ex: 1.70m): '))
IMC = peso / (altura ** 2)


if IMC < 25:
    print(f'\nPeso normal (IMC = {IMC:.2f}).')
else:
    print(f'\nAcima do peso (IMC = {IMC:.2f}).')