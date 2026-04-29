# 39. Escreva um programa que simula um menu com as opções:

# 1 - Somar dois números
# 2 - Subtrair dois números
# 3 - Sair
# O programa deve repetir o menu enquanto o usuário não escolher a opção 3.

print('*** MENU ***')
print('1 - Somar dois números')
print('2 - Subtrair dois números')
print('3 - Sair do programa')
print('*** ---- ***')
opção = int(input('\nSelecione uma opção: '))
        
while True:
    if opção < 3:
        print('*** MENU ***')
        print('1 - Somar dois números')
        print('2 - Subtrair dois números')
        print('3 - Sair do programa')
        print('*** ---- ***')
        print(f'\nOpção selecionada: {opção}')
        opção = int(input('Selecione uma opção: '))
    elif opção == 3:
        print('Você saiu do programa.')
        break
    elif opção > 3:
        print('*** MENU ***')
        print('1 - Somar dois números')
        print('2 - Subtrair dois números')
        print('3 - Sair do programa')
        print('*** ---- ***')
        print('\nOpção inválida.')
        opção = int(input('Selecione uma opção: '))