# 44. Leia três lados de um triângulo. 
# Verifique primeiro se formam um triângulo válido (cada lado deve ser menor que a soma dos outros dois). 
# Se válido, classifique como:

# "Equilátero" (três lados iguais)
# "Isósceles" (dois lados iguais)
# "Escaleno" (todos os lados diferentes)

print('*** CLASSIFICADOR DE TRIÂNGULOS ***')
lado1 = float(input('Digite a medida do lado 1: '))
lado2 = float(input('Digite a medida do lado 2: '))
lado3 = float(input('Digite a medida do lado 3: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:   
    if lado1 != lado2 != lado3:
        print('\nTriângulo Escaleno')

    if lado1 == lado2 != lado3 or lado1 != lado2 == lado3:
        print('\nTriângulo Isósceles') 

    if lado1 == lado2 == lado3:
        print('\nTriângulo Equilátero')