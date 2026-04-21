# 36. Leia a idade de uma pessoa e exiba a categoria:

# Idade < 12: "Criança"
# Idade < 18: "Adolescente"
# Idade < 60: "Adulto"
# Idade ≥ 60: "Idoso"

idade = int(input('Digite a sua idade: '))

if idade < 12:
    print('\nCriança')
elif idade < 18:
    print('\nAdolescente')
elif idade < 60:
    print('\nAdulto')
elif idade >= 60:
    print('\nIdoso')