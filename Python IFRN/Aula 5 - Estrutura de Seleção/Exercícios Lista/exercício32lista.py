# 32. Leia a nota de um aluno (0 a 10) e exiba o conceito:

# Nota ≥ 9: "A"
# Nota ≥ 7: "B"
# Nota ≥ 5: "C"
# Nota < 5: "D"

nota = int(input('Insira a nota (de 0 a 10): '))

if nota >= 9:
    print('\nConceito A')
elif nota >= 7:
    print('\nConceito B') 
elif nota >= 5: 
    print('\nConceito C')
elif nota < 5:
    print('\nConceito D')