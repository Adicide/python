# Questão 31 — Número de passos para zero (raiz digital)

# A raiz digital de um número é obtida somando repetidamente seus dígitos até restar um único dígito. 
# Leia N e imprima a raiz digital e o número de iterações necessárias.

# Exemplo:
# Entrada: 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2 → Raiz: 2, Iterações: 3

n = int(input('Digite um número: '))

n_str = str(n)
qntd_digitos_n = len(n_str)
iteracao = 0 # Número de iterações necessárias.
raiz_digital = 0


while qntd_digitos_n > 1:
    
    repeticao = 0   
    soma = 0
    while repeticao < qntd_digitos_n:
        soma += int(n_str[repeticao])
        repeticao += 1
    iteracao += 1
        
    soma_str = str(soma)
    n_str = soma_str
    qntd_digitos_soma = len(soma_str)
    if qntd_digitos_soma == 1:
        raiz_digital = soma
    qntd_digitos_n = qntd_digitos_soma

print(f'\nRaiz: {raiz_digital} / Iterações: {iteracao}')