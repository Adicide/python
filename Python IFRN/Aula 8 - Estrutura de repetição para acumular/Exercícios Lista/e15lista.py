# Questão 15 — Múltiplos de K 
# 
# Leia dois inteiros N e K. 
# Imprima todos os múltiplos de K no intervalo de 1 a N, um por linha. 

# Exemplo:

# Entrada: (N=20, K=3)
# Saída: 3 6 9 12 15 18

n = int(input('Digite um número: '))
k = int(input('Digite outro número: '))
print('')

multiplo = 0 
m = 0 # Fator de multiplicação 

while multiplo < n:
    m += 1
    multiplo = k * m
    
    if multiplo > n:
        break
    else:
        print(multiplo)