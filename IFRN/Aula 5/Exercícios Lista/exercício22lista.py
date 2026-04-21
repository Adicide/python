# 22. Leia o salário de uma pessoa. 
# Se o salário for maior que 3000, calcule e exiba o imposto de 15%; caso contrário, calcule e exiba o imposto de 7.5%.

print('*** CALCULADORA DE IMPOSTO ***') ; 
salário = float(input('Insira o seu salário: '))

imposto_015 = salário * 0.15
imposto_0075 = salário * 0.075

if salário > 3000:
    print(f'\nImposto: R${imposto_015:.2f}')
else:
    print(f'\nImposto: R${imposto_0075:.2f}')