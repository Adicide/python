# Questão 9 — Potências de 2

# Leia um número inteiro N. Imprima todas as potências de 2 menores ou iguais a N, começando por 1 (2⁰ = 1).

# Exemplo (N=100):

# Saída: 1 2 4 8 16 32 64

n = int(input('Digite um número: '))
print('')

potencia = 0 
resultado = 0

while resultado < n:
    resultado = 2 ** potencia
    
    if resultado > n:
        break
    else:
        print(resultado)
        
    potencia += 1