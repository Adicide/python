# 14. Escreva um programa que recebe um número inteiro base e um número inteiro positivo expoente, e calcula 
# base ** expoente sem usar o operador ** — use apenas multiplicações repetidas com while.

# Exemplo de entrada	Saída esperada
# base=2, expoente=8	256
# base=3, expoente=4	81

base = int(input('Insira um número que será a base: '))
expoente = int(input('Ótimo. Agora, insira um número positivo que será o expoente: '))

resultado = 1
potencia = 0 # Contador

while potencia < expoente:
    resultado *= base
    potencia += 1    
print(resultado)