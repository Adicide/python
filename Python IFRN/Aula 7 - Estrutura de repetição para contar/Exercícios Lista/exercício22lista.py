# 22. Escreva um programa que lê n notas de alunos (onde n é fornecido pelo usuário) e exibe a menor nota lida.

n = float(input('Digite a quantidade de notas: '))
print('')

repetições = 0
menor_nota = 999

while repetições < n:
    nota = float(input('Digite a nota do aluno: '))
    repetições += 1
    if nota < menor_nota:
        menor_nota = nota
print(f'\nA menor nota é: {menor_nota:.2f}')