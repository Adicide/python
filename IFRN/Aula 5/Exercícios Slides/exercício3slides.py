num1=int(input('\nInsira um número inteiro: '))
num2=int(input('Ótimo. Agora, insira outro: '))

somanums=num1+num2

if somanums % 2 == 0:
    print(f'\nA soma de {num1} e {num2} resulta em um número par ({somanums}).')
else:
    print(f'\nA soma de {num1} e {num2} resulta em um número ímpar ({somanums}).')