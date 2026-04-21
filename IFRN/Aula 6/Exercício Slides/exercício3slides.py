# Antes:
# --------------------------------------------
# n = int(input('Digite um inteiro: '))
# if n < 5:
# print('A entrada é maior do que cinco')
# else:
# print('A entrada é menor ou igual a cinco')

# Situação do erro: o programa imprime que a entrada é maior que 5 quando ela é, na verdade, menor que 5.

# Correto:
n = int(input('Digite um inteiro: '))
if n > 5:
    print('A entrada é maior do que cinco')
else:
    print('A entrada é menor ou igual a cinco')