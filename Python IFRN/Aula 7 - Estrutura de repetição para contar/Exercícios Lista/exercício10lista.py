# 10. Escreva um programa que lê 10 números reais digitados pelo usuário e imprime a média aritmética.

num1 = float(input('Digite o 1° número: '))
num2 = float(input('Digite o 2° número: '))
num3 = float(input('Digite o 3° número: '))
num4 = float(input('Digite o 4° número: '))
num5 = float(input('Digite o 5° número: '))
num6 = float(input('Digite o 6° número: '))
num7 = float(input('Digite o 7° número: '))
num8 = float(input('Digite o 8° número: '))
num9 = float(input('Digite o 9° número: '))
num10 = float(input('Digite o 10° número: '))

listanum = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
soma = 0 # Somatório dos números inseridos
a = 0 # Fator de adição

while a < len(listanum):
    soma += listanum[a]
    a += 1
média = soma / len(listanum)
print(f'\nMédia aritmética: {média}')