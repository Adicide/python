# Antes:
# ---------------------------------------------------------
# Programa que calcula as raízes de uma equação do 2º grau
# import math
# a = float(input('Coeficiente de x ao quadrado: ') )
# b = float(input('Coeficiente de x: '))
# c = float(input('Coeficiente livre: '))
# delta = b ** 2 - 4 * a * b
# if delta < 0:
# print('A equação não possui raízes reais.')
# elif delta == 0:
# x = -b / 2 * a
# print(f'Raíz: {x :. 4f}')
# else:
# x1 = -b + math.sqrt(delta) / 2 * a
# x2 = -b - math.sqrt(delta) / 2 * a
# print(f'Raiz 1: {x1 :. 4f}')
# print(f'Raiz 2: {x1 :. 4f}')

# Correto: 
import math

a = float(input('Coeficiente de x² (a): ') )
b = float(input('Coeficiente de x (b): '))
c = float(input('Coeficiente independente (c): '))
delta = b**2 - 4*a*c

if delta < 0:
    print('\nA equação não possui raízes reais.')
elif delta == 0:
    x = -b / 2 * a
    print(f'\nRaíz: {x:.4f}')
else:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a
    print(f'\nRaiz 1: {x1:.4f}')
    print(f'Raiz 2: {x2:.4f}')