# Questão 13 — Contagem de dígitos

# Leia um número inteiro positivo N. Imprima quantos dígitos ele possui.

# Exemplo:
# Entrada: 9087
# Saída: 4

n = int(input('Insira um número: '))
n_str = str(n)

repetiçao = 0
digitos = 0

while repetiçao < len(n_str):
    digitos += 1
    repetiçao += 1
print(f'\nQuantidade de dígitos de {n}: {digitos}')