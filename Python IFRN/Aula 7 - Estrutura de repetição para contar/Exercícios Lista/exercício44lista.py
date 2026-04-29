# 44. Escreva um programa que imprime uma escada de n degraus 
# usando o caractere *. Cada degrau i tem i asteriscos.

n = int(input('Digite um número: '))
print('')
i = '*' # Degrau
repetição = 0 # Contador

while repetição < n:
    print(i)
    i += '*'
    repetição += 1