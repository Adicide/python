# 10. Leia um número inteiro. Se ele for negativo, multiplique-o por -1 e exiba o resultado com a mensagem "Valor absoluto:".

num=int(input('\nDigite um número: '))
abs=num*-1

if num < 0:
    print(f'Valor absoluto: {abs}\n')