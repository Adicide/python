# Antes:
# ------------------------------------
# turno = int(input('Entrada: '))
# if turno == 'V' and turno == 'v':
# print('Vespertino')
# elif turno == 'M' and turno == 'm':
# print('Matutino')
# else:
# print('Valor inválido')

# Correto: 
turno = input('Entrada: ')

if turno == 'V' or turno == 'v':
    print('Vespertino')
elif turno == 'M' or turno == 'm':
    print('Matutino')
else:
    print('Valor inválido')