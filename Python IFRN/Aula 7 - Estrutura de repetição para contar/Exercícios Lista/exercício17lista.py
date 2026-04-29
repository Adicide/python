# 17. Escreva um programa que recebe dois inteiros positivos a e b (com a < b) 
# e imprime todos os inteiros no intervalo [a, b].

a = int(input('Digite um número: ')) # Contador
b = int(input('Digite outro número: '))

while a <= b:
    print(a)
    a += 1 # a = a + 1