# 49. Leia o ano e informe se é bissexto ou não. Um ano é bissexto se:

# For divisível por 400, ou
# For divisível por 4 e não divisível por 100.
# Exiba "Ano bissexto" ou "Ano não bissexto".

ano = int(input('Insira um ano: '))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print(f'\n{ano} é um Ano Bissexto.')
else:
    print(f'\n{ano} é um Ano não Bissexto')