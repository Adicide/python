# Questão 22 — Palíndromo numérico

# Leia um número inteiro positivo N. 
# Usando apenas operações aritméticas com while, determine se N é um palíndromo (lê-se igual de frente para trás).

# Exemplo:
# Entrada: 1221 → Saída: Palíndromo
# Entrada: 1234 → Saída: Não palíndromo

n = int(input('Digite um número: '))
n_str = str(n)

repetiçao = 0
inverso = ''
digitos_n = len(n_str)
while repetiçao < digitos_n:
    inverso += n_str[digitos_n - 1 - repetiçao]
    repetiçao += 1

inverso_int = int(inverso)
if inverso_int == n:
    print(f'\n{n} É um Palíndromo.')
else: 
    print(f'\n{n} Não é um palíndromo.')