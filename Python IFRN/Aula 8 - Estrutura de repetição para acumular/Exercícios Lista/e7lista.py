# Questão 7 — Contagem de pares e ímpares

# Leia N números inteiros. Conte quantos são pares e quantos são ímpares. Imprima os dois resultados.

# Exemplo (N=5, valores: 1, 2, 3, 4, 5):

# Saída: Pares: 2 / Ímpares: 3

n = int(input('Digite a quantidade de números a serem lidos: '))
print('')

repetição = 0
pares = 0
ímpares = 0
while repetição < n:
    num = int(input('Digite um número: '))
    
    if num % 2 == 0:
        pares += 1
    else:
        ímpares += 1
        
    repetição += 1
print(f'\nQuantidade de números pares: {pares}')
print(f'Quantidade de números ímpares: {ímpares}')