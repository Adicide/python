# Questão 34 — Exponenciação modular

# Leia três inteiros B, E e M. Calcule B^E mod M usando o método de exponenciação por quadratura iterativa com while (sem usar pow(B, E, M)). Imprima o resultado.

# Exemplo:
# Entrada: 2 10 1000
# Saída: 24

b = int(input('Digite o número da base: '))
e = int(input('Digite o número do expoente: '))
m = int(input('Digite o número do módulo: '))

resultado = 1
base = b % m
while e > 0:
    if e % 2 == 1:
        resultado = (resultado * base) % m
    base = (base * base) % m
    e //= 2
print(f'Resultado: {resultado}\n')