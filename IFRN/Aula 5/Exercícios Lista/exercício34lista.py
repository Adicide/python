# 34. Leia o IMC de uma pessoa e classifique:

# IMC < 18.5: "Abaixo do peso"
# IMC < 25: "Peso normal"
# IMC < 30: "Sobrepeso"
# IMC ≥ 30: "Obesidade"

print('*** CALCULADORA DE IMC ***')
peso = float(input('Insira seu peso em kg (ex: 70kg): '))
altura = float(input('Insira sua altura em m (ex: 1.70m): '))
IMC = peso / (altura ** 2)

if IMC < 18.5:
    print(f'\nAbaixo do peso (IMC = {IMC:.2f}).')
elif IMC < 25:
    print(f'\nPeso normal (IMC = {IMC:.2f}).')
elif IMC < 30:
    print(f'\nSobrepeso (IMC = {IMC:.2f}).')
elif IMC >= 30:
    print(f'\nObesidade (IMC = {IMC:.2f}).')