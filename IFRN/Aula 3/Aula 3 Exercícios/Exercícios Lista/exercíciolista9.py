# Exercício 9 — Hipotenusa de um triângulo retângulo (math.sqrt())
# Dado um triângulo retângulo, a hipotenusa pode ser calculada pela 
# fórmula: h = sqrt(a² + b²). Escreva um programa que leia os dois catetos e calcule e imprima a hipotenusa. 

# Exemplo de entrada e saída:
# Digite o valor do cateto a: 3
# Digite o valor do cateto b: 4
# A hipotenusa é: 5.0

import math

print('*** Calculadora de Hipotenusa ***')

cat1=float(input('Medida do 1° cateto: '))
cat2=float(input('Medida do 2° cateto: '))

h=math.sqrt(cat1**2 + cat2**2)

print(f'\nA hipotenusa desse triângulo é: {h}', f'\n*** ------------------------- ***')