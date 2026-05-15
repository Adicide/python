# Questão 19 — Conversão de base: decimal para binário

# Leia um número inteiro não-negativo N. Converta-o para a representação binária usando divisões sucessivas por 2. Imprima o resultado binário como uma string.

# Exemplo:
# Entrada: 13
# Saída: 1101

n = int(input('Digite um número: '))
n_original = n

binário = ''

while n > 0:
    r = n % 2
    binário = str(r) + binário
    n //= 2
    
print(f'{n_original} em binário: {binário}')