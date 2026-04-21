# 7. Leia o nome de um usuário. Se o nome tiver mais de 10 caracteres, exiba "Nome muito longo".

nome_usuário = str(input('Digite o seu nome de usuário: ')) 

if len(nome_usuário) > 10:
    print('\nNome muito longo.')