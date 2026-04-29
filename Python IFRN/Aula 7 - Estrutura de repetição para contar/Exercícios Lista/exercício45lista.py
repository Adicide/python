# 45. Escreva um programa que recebe dois inteiros inicio e fim 
# e exibe a soma de todos os números primos no intervalo [inicio, fim].

início = int(input('Digite um número: ')) # 1° Número
fim = int(input('Digite outro número: ')) # 2° Número
repetição = início
soma_primos = 0


while repetição <= fim:
    
    if repetição == 2:
        primo = True
    elif repetição < 2:
        primo = False
    elif repetição > 2:
        primo = True
        divisor = 2
        # Esse loop de baixo vai calcular se a variável 'repetições' é, de fato, primo. Ele só quebra se ela não for um número primo.
        while divisor * divisor <= repetição: 
            if repetição % divisor == 0:
                primo = False
                break
            divisor += 1
    
    if primo == True:
        soma_primos += repetição
        
    repetição += 1
print(f'\nA soma dos números primos de {início} até {fim} é: {soma_primos}')