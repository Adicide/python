# 33. Leia um número inteiro de 1 a 7 representando um dia da semana e exiba o nome do dia correspondente 
# (1 = Segunda, 2 = Terça, …, 7 = Domingo). Se o valor estiver fora do intervalo, exiba "Dia inválido".

num = int(input('Digite um número de 1 a 7: '))

if num == 1: 
    print('1 = Segunda')
elif num == 2: 
    print('2 == Terça')
elif num == 3:
    print('3 = Quarta')
elif num == 4:
    print('4 = Quinta')
elif num == 5:
    print('5 = Sexta')
elif num == 6: 
    print('6 = Sábado')
elif num == 7:
    print('7 = Domingo')
else:
    print('Dia inválido.')