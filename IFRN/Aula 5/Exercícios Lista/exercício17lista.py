# 17. Leia a idade de uma pessoa. Se ela for maior ou igual a 18, exiba "Maior de idade"; caso contrário, exiba "Menor de idade".

idade = int(input('Olá! Digite a sua idade: '))

if idade >= 18: 
    print(f'\nVocê é Maior de Idade.')
else:
    print(f'\nVocê é Menor de Idade.')