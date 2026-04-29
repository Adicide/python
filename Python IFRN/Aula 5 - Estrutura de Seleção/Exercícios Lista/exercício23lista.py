# 23. Leia uma senha digitada pelo usuário. 
# Compare com a senha "python2026". 
# Se for correta, exiba "Acesso permitido"; caso contrário, exiba "Acesso negado".

senha = input('Insira sua senha: ')

if senha == 'python2026':
    print('\nAcesso permitido.')
else:
    print('\nAcesso negado.')