# 21. Escreva um programa que lê n notas de alunos 
# (onde n é fornecido pelo usuário) e exibe a maior nota lida. USE APENAS O WHILE

n = float(input('Digite a quantidade de notas: '))
print('')

contador = 0
maior_nota = 0

while contador < n:
    nota = float(input('Digite a nota do aluno: '))
    contador += 1
    if nota > maior_nota:
        maior_nota = nota
print(f'\nA maior nota é: {maior_nota:.2f}')