# 39. Leia o salário de um funcionário e calcule o reajuste:

# Salário ≤ 1500: reajuste de 15%
# Salário ≤ 3000: reajuste de 10%
# Salário ≤ 6000: reajuste de 7%
# Salário > 6000: reajuste de 3%

# Exiba o novo salário.

print('*** REAJUSTE DE SALÁRIO ***')
salário = float(input('Digite seu salário: '))

if salário <= 1500:
    reajuste = salário * 0.15
    print(f'\nReajuste de 15% => Reajuste = R${reajuste:.2f}')
if salário <= 3000:
    reajuste = salário * 0.10
    print(f'\nReajuste de 10% => Reajuste = R${reajuste:.2f}')
if salário <= 6000:
    reajuste = salário * 0.07
    print(f'\nReajuste de 7% => Reajuste = R${reajuste:.2f}')
if salário > 6000:
    reajuste = salário * 0.03
    print(f'\nReajuste de 3% => Reajuste = R${reajuste:.2f}')