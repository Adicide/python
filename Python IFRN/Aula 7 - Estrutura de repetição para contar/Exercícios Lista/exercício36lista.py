# 36. Escreva um programa que lê uma senha digitada pelo usuário e continua pedindo a senha enquanto ela estiver incorreta. 
# A senha correta é "python123". Ao acertar, exibe "Acesso permitido".

senha = 'python123'
acesso = input('Digite a senha: ')

while True:
    if acesso != senha:
        print('\nAcesso negado.')
        acesso = input('Digite a senha: ')
    else:
        print('\nAcesso permitido.')
        break