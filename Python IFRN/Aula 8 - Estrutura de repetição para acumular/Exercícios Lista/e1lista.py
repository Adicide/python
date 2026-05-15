# Questão 1 — Contagem regressiva

# Leia um número inteiro positivo N. Imprima todos os números de N até 1 em ordem decrescente, um por linha. Ao final, imprima Fogo!.

# Exemplo:
# Entrada: 5
# Saída: 5 4 3 2 1 Fogo!

n = int(input('Digite um número: '))
print('')
n_original = n

repetição = 0
while repetição < n_original:
    print(n)
    n -=1
    repetição += 1
print('Fogo!')