# 28. Escreva um programa FizzBuzz: imprima os inteiros de 1 a 30, mas substitua:

# os múltiplos de 3 pela palavra Fizz,
# os múltiplos de 5 pela palavra Buzz,
# os múltiplos de 3 e 5 pela palavra FizzBuzz.

repetições = 0

while repetições < 30:
    repetições += 1
    if repetições % 3 == 0 and repetições % 5 == 0:
        print('FizzBuzz')
    elif repetições % 3 == 0: 
        print('Fizz')
    elif repetições % 5 == 0:
        print('Buzz')
    else:
        print(repetições)