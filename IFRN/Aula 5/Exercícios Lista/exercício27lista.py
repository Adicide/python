# 27. Leia o ano de nascimento de uma pessoa. 
# Se a pessoa tiver 65 anos ou mais em 2026, exiba "Elegível para aposentadoria"; 
# caso contrário, exiba "Não elegível ainda".

print('*** ELEGIBILIDADE DE APOSENTADORIA ***')
ano_nascimento = int(input('Digite seu ano de nascimento: '))

if 2026 - ano_nascimento >= 65:
    print('\nVocê está Elegível para aposentadora.')
else:
    print('\nVocê não é elegível ainda.')