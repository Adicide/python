# 43. Um cinema cobra ingressos de acordo com a idade:

# Crianças até 5 anos: gratuito
# De 6 a 12 anos: R$ 12,00
# De 13 a 17 anos: R$ 18,00
# 18 anos ou mais: R$ 25,00

# Leia a idade e exiba o valor do ingresso.

print('*** INGRESSOS ***')
print('Crianças até 5 anos: gratuito')
print('De 6 a 12 anos: R$ 12,00')
print('De 13 a 17 anos: R$ 18,00')
print('18 anos ou mais: R$ 25,00')

idade = int(input('\nDigite sua idade: '))

if idade <= 5:
    print('Ingresso: Gratuito')
elif 6 <= idade <= 12:
    print('Ingresso: R$12.00')
elif 13 <= idade <= 17:
    print('Ingresso: R$18.00')
elif idade >= 18:
    print('Ingresso: R$25.00')