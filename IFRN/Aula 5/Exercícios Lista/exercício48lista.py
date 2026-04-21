# 48. Leia o consumo mensal de energia elétrica (em kWh) de uma residência e calcule o valor da conta conforme a tabela:

# Até 100 kWh: R$ 0,40 por kWh
# De 101 a 200 kWh: R$ 0,50 por kWh
# De 201 a 300 kWh: R$ 0,65 por kWh
# Acima de 300 kWh: R$ 0,85 por kWh
# Exiba o valor total a pagar.

consumo_mensal = int(input('Digite o seu consumo mensal em kWh: '))

if consumo_mensal <= 100:
    valor = consumo_mensal * 0.40
    print(f'\nValor total da conta: R${valor:.2f}')
if 101 <= consumo_mensal <= 200:
    valor = consumo_mensal * 0.50
    print(f'\nValor total da conta: R${valor:.2f}')
if 201 <= consumo_mensal <= 300:
    valor = consumo_mensal * 0.65
    print(f'\nValor total da conta: R${valor:.2f}')
if consumo_mensal > 300:
    valor = consumo_mensal * 0.85
    print(f'\nValor total da conta: R${valor:.2f}')