# 41. Leia três números inteiros e exiba-os em ordem crescente usando apenas estruturas de seleção.

# Casos possíveis:
# num1 num2 num3 V
# num1 num3 num2 V
# num2 num1 num3 V
# num2 num3 num1 V
# num3 num1 num2 V
# num3 num2 num1 V

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 >= num2 >= num3:
    print(f'\nNúmeros em ordem crescente: {num3} ; {num2} ; {num1}')
elif num1 >= num3 >= num2:
    print(f'\nNúmeros em ordem crescente: {num2} ; {num3} ; {num1}')
elif num2 >= num1 >= num3:
    print(f'\nNúmeros em ordem crescente: {num3} ; {num1} ; {num2}')
elif num2 >= num3 >= num1:
    print(f'\nNúmeros em ordem crescente: {num1} ; {num3} ; {num2}')
elif num3 >= num1 >= num2:
    print(f'\nNúmeros em ordem crescente: {num2} ; {num1} ; {num3}')
elif num1 <= num2 <= num3:
    print(f'\nNúmeros em ordem crescente: {num1} ; {num2} ; {num3}')