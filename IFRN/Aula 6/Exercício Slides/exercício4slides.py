# Antes:
# ---------------------------------------------------------------
# Programa que informa se a entrada é um múltiplo de 3 e/ou de 5
# n = int(input('Entrada:'))
# if n % 3 == 0:
# print(f'{n} é múltiplo de 3')
# elif n % 5 == 0:
# print(f'{n} é múltiplo de 5')
# elif n % 3 == 0 and n % 5 == 0:
# print(f'{n} é múltiplo de 3 e de 5')
# else:
# print(f'{n} não é múltiplo nem de 3 nem de 5')

# Situação de erro: O erro estava nas condições if, else e elif, que estavam analisando apenas se o número era múltiplo ou por 3 ou por 5,
# sem imprimi-lo no caso dele ser múltiplo dos dois. (Ex: 15 é múltiplo dos dois, mas o programa só imprimia que ele era múltiplo de 3.)

# Correto:
n = int(input('Entrada:'))

if n % 3 == 0 and n % 5 == 0:
    print(f'{n} é múltiplo de 3 e de 5')
elif n % 3 != 0 and n % 5 != 0:
    print(f'{n} não é múltiplo nem de 3 nem de 5')
else:
    if n % 3 == 0:
        print(f'{n} é múltiplo de 3')
    if n % 5 == 0:
        print(f'{n} é múltiplo de 5')