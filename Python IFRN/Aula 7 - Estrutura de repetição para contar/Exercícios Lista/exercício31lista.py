# 31. Escreva um programa que lê 10 notas (de 0 a 10) e exibe:

# a média das notas,
# a quantidade de alunos aprovados (média ≥ 7),
# a quantidade de alunos reprovados (média < 5),
# a quantidade de alunos em recuperação (5 ≤ média < 7).

n = 0 # Quantidade de notas
soma_notas = 0 # Soma total de todas as notas
aprovados = 0
reprovados = 0
recuperação = 0

while n < 10:
    nota = float(input('Digite uma nota:')) # Nota de cada aluno
    soma_notas += nota
    if nota >= 7:
        aprovados += 1
    elif nota >= 5:
        recuperação += 1
    elif nota < 5:
        reprovados += 1
        
    n += 1
    
média = soma_notas / n # Média total

print(f'Média: {média}')
print(f'Quantidade de alunos aprovados: {aprovados}')
print(f'Quantidade de alunos em recuperação: {recuperação}')
print(f'Quantidade de alunos reprovados: {reprovados}')  