# *** ESPAÇO PARA TESTES ***

n = int(input('Entrada:'))

if n % 3 == 0:
    print(f'{n} é múltiplo de 3')
elif n % 5 == 0:
    print(f'{n} é múltiplo de 5')
elif n % 3 == 0 and n % 5 == 0:
    print(f'{n} é múltiplo de 3 e de 5')
else:
    print(f'{n} não é múltiplo nem de 3 nem de 5')