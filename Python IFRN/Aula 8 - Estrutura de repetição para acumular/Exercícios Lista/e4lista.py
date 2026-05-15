# Questão 4 — Fatorial

# Leia um número inteiro não-negativo N. Calcule e imprima o valor de N! (fatorial de N). Considere que 0! = 1.

# Exemplo:

# Entrada: 5
# Saída: 120

n = int(input('Digite um número: '))
n_original = n
fatorial = 1

while n > 0:
    fatorial *= n
    n -= 1
    
print(f'\n{n_original}! = {fatorial}')