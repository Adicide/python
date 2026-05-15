# Questão 16 — Sequência de Collatz

# Dado um número inteiro positivo N, aplique a seguinte regra repetidamente até chegar em 1: 
# Se N for par, divida por 2; 
# Se for ímpar, multiplique por 3 e some 1. 

# Imprima cada valor da sequência (incluindo o inicial e o 1 final) e o número total de passos.

# Exemplo (N=6):

# Sequência: 6 3 10 5 16 8 4 2 1
# Passos: 8

n = int(input('Digite um número: '))

sequencia = str(n)
passos = 0

while n != 1:
    
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
    
    sequencia += ' ' + str(n)
    passos += 1

print(f'\nSequência: {sequencia}')
print(f'Passos: {passos}')