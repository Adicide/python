# 46. Escreva um programa que lê n números reais e classifica cada um como:

# "pequeno" se o valor for menor que 10,
# "médio" se o valor estiver entre 10 e 100 (inclusive),
# "grande" se o valor for maior que 100.

# Ao final, exibe a contagem de cada categoria.

n = int(input('Digite a quantidade de números a serem lidos: '))
repetição = 0

pequenos = 0
médios = 0
grandes = 0

while repetição < n:
    num = float(input('\nDigite um número: '))
    if num < 10:
        print(f'{num} é Pequeno.')
        pequenos += 1
    elif 10 <= num <= 100:
        print(f'{num} é Médio.')
        médios += 1
    elif num > 100:
        print(f'{num} é Grande.')
        grandes += 1
    repetição += 1

print(f'\nQuantidade de números pequenos: {pequenos}')
print(f'Quantidade de números médios: {médios}')
print(f'Quantidade de números grandes: {grandes}')