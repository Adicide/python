# Questão 8 — Maior e menor valor

# Leia N números inteiros (N ≥ 1). Encontre e imprima o maior e o menor valor entre eles.

# Exemplo (N=4, valores: 3, 7, 1, 5):
# Saída: Maior: 7 / Menor: 1

n = int(input('Digite a quantidade de números a serem lidos: '))
print('')

repetição = 0
listanums = []
while repetição < n:
    num = int(input('Digite um número: '))
    listanums.append(num)
    repetição += 1
print(f'\nMaior número: {max(listanums)}')
print(f'Menor número: {min(listanums)}')