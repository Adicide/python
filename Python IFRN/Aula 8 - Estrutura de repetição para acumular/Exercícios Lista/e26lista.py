# Questão 26 — Contagem de divisores

# Leia um inteiro positivo N. Conte e imprima o número de divisores positivos de N (incluindo 1 e N).

# Exemplo:
# Entrada: 12
# Saída: 6 (divisores: 1, 2, 3, 4, 6, 12)

n = int(input('Digite um número: '))

divisor = 1 
qntd_divisores = 0 # Quantidade de divisores de n
série_divisores = '' 

while divisor <= n:
    if n % divisor == 0:
        qntd_divisores += 1
        divisor_str = str(divisor)
        série_divisores += divisor_str + ', '
    divisor += 1 
série_divisores  = série_divisores[:-2]
print(f'\nQuantidade de divisores de {n}: {qntd_divisores} ({série_divisores})')
