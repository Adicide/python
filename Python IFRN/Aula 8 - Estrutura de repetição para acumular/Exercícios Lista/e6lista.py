# Questão 6 — Soma até sentinela

# Leia números inteiros um por vez até que o usuário digite 0. Imprima a soma de todos os números lidos (excluindo o zero).

# Exemplo 
# (Entrada: 3, 7, 2, -1, 0):
# Saída: 11

soma_nums = 0
while True:
    n = int(input('Digite um número: '))
    
    if n == 0:
        break
    
    soma_nums += n
print(f'\nA soma de todos os números é {soma_nums}')