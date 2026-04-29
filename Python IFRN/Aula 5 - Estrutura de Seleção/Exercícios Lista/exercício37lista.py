# 37. Leia o mês (1 a 12) e exiba a estação do ano correspondente no hemisfério sul:

# Meses 12, 1, 2: "Verão"
# Meses 3, 4, 5: "Outono"
# Meses 6, 7, 8: "Inverno"
# Meses 9, 10, 11: "Primavera"
# Valor fora do intervalo: "Mês inválido"

mês = int(input('Insira o mês (de 1 a 12): '))

if mês == 12 or mês == 1 or mês == 2:
    print('\nVerão')
elif mês == 3 or mês == 4 or mês == 5:
    print('\nOutono')
elif mês == 6 or mês == 7 or mês == 8:
    print('\nInverno')
elif mês == 9 or mês == 10 or mês == 11:
    print('\nPrimavera')
else:
    print('\nMês inválido.')