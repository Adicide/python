# 30. Leia uma string. Se ela tiver mais de 5 caracteres, exiba a string em maiúsculas; 
# caso contrário, exiba-a em minúsculas.

palavra = str(input('Digite uma palavra: '))
maiúscula = palavra.upper()
minúscula = palavra.lower()

if len(palavra) > 5:
    print(f'\n{maiúscula}')
else:
    print(f'\n{minúscula}')