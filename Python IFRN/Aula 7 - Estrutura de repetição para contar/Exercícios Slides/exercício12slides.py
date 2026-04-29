n = int(input('Digite um número: '))
x = 0

while x < n:
    x = x + 1
    if x % 3 == 0 and x % 4 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 4 == 0:
        print('Buzz')
    else: 
        print(x)