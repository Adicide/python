# 24. Leia dois números reais. 
# Calcule e exiba a divisão do primeiro pelo segundo. 
# Se o segundo for zero, exiba "Divisão por zero não é permitida".

print('*** DIVISÃO ***')
num1 = float(input('Insira um número: '))
num2 = float(input('Insira outro número: '))

if num2 == 0:
    print('\nDivisão por zero não é permitida.')
else:
    divisão_nums = num1 / num2 
    print(f'\n{num1} ÷ {num2} = {divisão_nums}')