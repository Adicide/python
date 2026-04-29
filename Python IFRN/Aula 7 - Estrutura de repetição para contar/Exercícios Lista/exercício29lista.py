# 29. Escreva um programa que lê n números reais 
# e exibe separadamente a soma dos valores positivos e a soma dos valores negativos.

n = int(input('Digite a quantidade de números a serem lidos: '))
print('')
repetições = 0
soma_positivos = 0
soma_negativos = 0

while repetições < n:
    número = float(input('Digite um número: '))
    if número > 0:
        soma_positivos += número
    elif número < 0:
        soma_negativos += número
    
    repetições += 1
        
print(f'\nSoma dos positivos: {soma_positivos}')
print(f'Soma dos negativos: {soma_negativos}')