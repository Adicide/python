# 38. Leia dois números e um operador (+, -, *, /). 
# Realize a operação correspondente e exiba o resultado. 
# Se o operador for / e o divisor for 0, exiba mensagem de erro. Se o operador for inválido, exiba "Operador inválido".

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
operador = str(input('Insira um operador: '))

if operador == '+':
    resultado = num1 + num2
    print(f'\nResultado = {resultado}')
elif operador == '-':
    resultado = num1 - num2
    print(f'\nResultado = {resultado}')
elif operador == '*':
    resultado = num1 * num2
    print(f'\nResultado = {resultado}')
elif operador == '/':
    if num2 == 0:
        print('\nERRO: A DIVISÃO POR ZERO NÃO É PERMITIDA.')
    else:
        resultado = num1 / num2
        print(f'\nResultado: {resultado}')
else:
    print('\nOperador inválido.')