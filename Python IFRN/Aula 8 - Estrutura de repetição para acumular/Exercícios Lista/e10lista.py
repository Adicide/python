# Questão 10 — Sequência de Fibonacci

# Leia um número inteiro positivo N. Imprima os N primeiros termos da sequência de Fibonacci (começando por 0 e 1).

# Exemplo (N=7):

# Saída: 0 1 1 2 3 5 8

n = int(input('Digite um número: '))
print(f'\n{n} primeiros termos da Sequência de Fibonacci: ')

a = 0
b = 1
repetiçao = 0

while repetiçao < n:
    print(a)
    soma = a + b
    a = b
    b = soma
    repetiçao += 1  