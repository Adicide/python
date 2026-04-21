# 47. Leia uma nota de 0 a 100 (inteiro) e classifique:

# 90 a 100: "Excelente"
# 70 a 89: "Bom"
# 50 a 69: "Regular"
# 0 a 49: "Insuficiente"
# Fora do intervalo: "Nota inválida"

nota = int(input('Digite a sua nota: '))

if nota < 0 or nota > 100:
    print('\nNota inválida.')
else:
    if 0 <= nota <= 49:
        print('\nInsuficiente.')
    elif 50 <= nota <= 69:
        print('\nRegular.')
    elif 70 <= nota <= 89:
        print('\nBom.')
    elif 90 <= nota <= 100:
        print('\nExcelente.')