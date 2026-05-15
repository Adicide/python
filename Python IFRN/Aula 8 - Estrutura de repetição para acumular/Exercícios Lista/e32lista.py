# Questão 32 — Crivo simplificado: primos em um intervalo

# Leia dois inteiros A e B (A ≤ B). Imprima todos os números primos no intervalo [A, B], um por linha. 
# Ao final, informe a quantidade total de primos encontrados.

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
print('')

while a > b:
    print('\nERRO: O primeiro número deve ser menor ou igual ao segundo.')
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    
    if a <= b:
        print('')
        continue
    
repeticao = a
qntd_primo = 0 
while repeticao <= b:
    if repeticao <= 1:
        primo = False
    elif repeticao == 2:
        primo = True
    else:
        primo = True
        divisor = 2
        
        while divisor < repeticao:
            if repeticao % divisor == 0:
                primo = False
                break
            divisor += 1
            
    if primo: 
        print(repeticao)
        qntd_primo += 1
        
    repeticao += 1
print(f'Quantitade de números primos: {qntd_primo}')