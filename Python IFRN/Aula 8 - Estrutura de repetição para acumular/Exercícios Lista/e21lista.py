# Questão 21 — Número de Armstrong

# Um número de n dígitos é de Armstrong (ou narcisista) 
# se a soma de seus dígitos elevados à n-ésima potência for igual ao próprio número. 
# Leia N inteiros e informe se cada um é ou não de Armstrong.

# Exemplo:
# Entrada: 153 → Saída: Armstrong (1³ + 5³ + 3³ = 153)
# Entrada: 100 → Saída: Não Armstrong

N = int(input('Digite a quantidade de números a serem lidos: '))
print('')

repetiçao_loop1 = 0
while repetiçao_loop1 < N:
    num = int(input('Insira um número: '))
    num_str = str(num)
    digitos_num = len(num_str) # Quantidade de dígitos da string do número
    
    repetiçao_loop2 = 0 # Repetição do 2° loop
    soma_digitos = 0
    while repetiçao_loop2 < digitos_num:
        digito = int(num_str[repetiçao_loop2])  # Lê o dígito
        soma_digitos += digito ** digitos_num # Eleva o dígito a n e depois coloca na soma
        repetiçao_loop2 += 1
    
    if soma_digitos == num:
        print(f'{num} É um número de Armstrong.\n')
    else:
        print(f'{num} Não é um número de Armstrong.\n')
        
    repetiçao_loop1 += 1