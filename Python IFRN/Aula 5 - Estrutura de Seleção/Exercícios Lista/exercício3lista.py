# 3. Leia dois números inteiros. Se o primeiro for maior que o segundo, exiba "O primeiro número é maior".

num1 = int(input('\nDigite um número: '))
num2 = int(input('Ótimo. Agora digite outro: '))

if num1 > num2:
    print(f'\nO primeiro número ({num1}) é maior.')