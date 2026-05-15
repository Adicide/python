# Questão 5 — Média de notas

# Leia N notas de alunos (valores reais entre 0 e 10). Calcule e imprima a média aritmética com duas casas decimais.

# Exemplo (N=4, notas: 7.0, 8.5, 6.0, 9.5):

# Saída: 7.75

n = int(input('Digite a quantidade de notas a serem lidas: '))
print('')

repetição = 0
soma_notas = 0

while repetição < n:
    nota = float(input('Insira uma nota entre 0 e 10: '))
    if nota < 0 or nota > 10:
        print('Nota inválida!\n')
        continue
    soma_notas += nota
    repetição += 1
    
média = soma_notas / n
print(f'\nMédia: {média:.2f}')