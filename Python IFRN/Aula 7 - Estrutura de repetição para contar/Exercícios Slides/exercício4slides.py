iniciar = input('Iniciar? Digite Sim ou Não: ')

if iniciar == 'Sim':
    print('')
    x = 0
    while x < 30:
        x = x + 1
        print(x)
elif iniciar == 'Não':
    print('\nPrograma encerrado.')