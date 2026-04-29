# 35. Leia a velocidade de um carro e exiba a multa correspondente:

# Velocidade ≤ 80 km/h: "Sem multa"
# Velocidade ≤ 100 km/h: "Multa leve: R$ 130"
# Velocidade ≤ 120 km/h: "Multa média: R$ 195"
# Velocidade > 120 km/h: "Multa grave: R$ 293 + suspensão" 

velocidade = float(input('Insira a velocidade do carro (km/h): '))

if velocidade <= 80:
    print('\nSem multa.')
elif velocidade <= 100:
    print('\nMulta leve: R$130.00')
elif velocidade <= 120:
    print('\nMulta média: R$195.00')
elif velocidade > 120:
    print('\nMulta grave: R$293.00 + suspensão.')