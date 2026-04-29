# 46. Leia dois números inteiros e uma operação:

# 1 para encontrar o maior
# 2 para encontrar o menor
# 3 para calcular a soma
# 4 para calcular a diferença
# Exiba o resultado ou "Opção inválida" se a opção não existir.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

operação = int(input('Digite um número para realizar uma operação: '))

listanum = [num1, num2]
soma = num1 + num2
diferença = num1 - num2

if operação == 1:
    print(f'\nMaior número: {max(listanum)}')
elif operação == 2:
    print(f'\nMenor número: {min(listanum)}')
elif operação == 3:
    print(f'\nSoma: {soma}')
elif operação == 4:
    print(f'\nDiferença: {diferença}')
elif operação <= 0 or operação > 4:
    print('\nOpção inválida.')