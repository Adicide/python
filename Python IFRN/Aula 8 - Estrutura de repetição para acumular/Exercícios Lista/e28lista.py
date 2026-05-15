# Questão 28 — Número digital persistente

# A persistência multiplicativa de um número é o número de vezes que se deve multiplicar seus dígitos
# até obter um único dígito. Leia N e calcule sua persistência multiplicativa.

# Exemplo:
# Entrada: 39 → 3 × 9 = 27 → 2 × 7 = 14 → 1 × 4 = 4 → Persistência: 3

n = int(input('Digite um número: '))
n_str = str(n)
digitos_n = len(n_str)

persistencia = 0

if digitos_n == 1:
    print(f'Persistência multiplicativa do {n}: {persistencia}\n')
elif digitos_n > 1:
    repeticao = 0
    operacao = 1
    while repeticao < digitos_n:
        operacao *= int(n_str[repeticao])
        repeticao += 1
    persistencia += 1

    operacao_str = str(operacao)
    digitos_operacao = len(operacao_str)

    while digitos_operacao > 1:
        repeticao = 0
        operacao = 1
        
        while repeticao < digitos_operacao:
            operacao *= int(operacao_str[repeticao])
            repeticao += 1
        persistencia += 1
            
        operacao_str = str(operacao)
        digitos_operacao = len(operacao_str)
    print(f'Persistência multiplicativa do {n}: {persistencia}\n')