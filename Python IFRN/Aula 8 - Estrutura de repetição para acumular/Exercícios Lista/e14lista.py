# Questão 14 — Número primo

# Leia um número inteiro N (N ≥ 2). Determine se ele é primo ou não. Imprima Primo ou Não primo.

# Exemplo:
# Entrada: 17
# Saída: Primo

n = int(input('Digite um número: '))


if n < 2:
    primo = False
elif n == 2:
    primo = True
else: 
    primo = True
    divisor = 2
    while divisor < n:
        if n % divisor == 0:
            primo = False
            break
        divisor += 1

if primo == True:
    print(f'\n{n} é Primo.')
else:
    print(f'\n{n} Não é primo.')