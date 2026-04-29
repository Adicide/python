# Antes:  
# ---------------------------------------
# a = int(input('Digite o dividendo: '))
# b = int(input('Digite o divisor: '))
# q = a / b
# print('Quociente:', q)


# Correto:
a = int(input('Digite o dividendo: '))
b = int(input('Digite o divisor: '))

if b == 0:
    print('\nERRO: Divisão por zero não é permitida.')
else:
    q = a / b
    print('\nQuociente:', q)