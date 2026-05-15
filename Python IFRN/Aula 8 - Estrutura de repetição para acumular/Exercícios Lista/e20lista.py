# Questão 20 — Número perfeito

# Um número inteiro positivo é perfeito se a soma de seus divisores próprios (excluindo ele mesmo) for igual a ele. Leia N inteiros positivos e, para cada um, informe se é perfeito ou não.

# Exemplo:

# Entrada: 6 → Saída: Perfeito (1+2+3=6)
# Entrada: 10 → Saída: Não perfeito

n = int(input('Digite um número: '))

repetição = 0
divisor = 0 
soma_divisores = 0

while repetição < n:
    divisor += 1
    if n % divisor == 0 and divisor < n:
        soma_divisores += divisor
    repetição += 1

if soma_divisores == n:
    print(f'\n{n} é Perfeito.')
else:
    print(f'\n{n} Não é perfeito.')