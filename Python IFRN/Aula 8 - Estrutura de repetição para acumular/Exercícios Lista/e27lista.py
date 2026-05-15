# Questão 27 — Soma dos números primos até N

# Leia um inteiro positivo N. Calcule e imprima a soma de todos os primos menores ou iguais a N.

# Exemplo (N=10):
# Saída: 17 (2+3+5+7)

n = int(input('Digite um número: '))

num = 0 # Serve como o contador (ou 'repetição')
soma_primos = 0
sequencia_primos = ''

while num <= n:
    
    if num < 2:
        primo = False  
    elif num == 2:
        primo = True
    else:
        primo = True
        divisor = 2
        
        while divisor < num:
            if num % divisor == 0:
                primo = False
                break
            divisor += 1
    
    if primo == True:
        soma_primos += num
        num_str = str(num)
        sequencia_primos += num_str + ' + '
    num += 1

sequencia_primos = sequencia_primos[:-3]
print(f'\nSoma dos números primos até {n}: {soma_primos} ({sequencia_primos})')