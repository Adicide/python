# Questão 29 — Sequência de soma acumulada com filtro

# Leia inteiros um por vez até que a soma acumulada supere 1000. Considere apenas os valores positivos para a soma. 
# Imprima quantos números foram lidos no total e quantos eram positivos.

# Exemplo (entrada: 200, -50, 300, 600):
# Saída: Total lidos: 4 / Positivos: 3

soma = 0
total_nums = 0 # Total de números lidos
total_positivos = 0 # Total de números positivos

while soma < 1000:
    num = int(input('Digite um número: '))
    total_nums += 1
    if num > 0:
        soma += num
        total_positivos += 1
print(f'\nTotal lidos: {total_nums} / Total Positivos: {total_positivos}')