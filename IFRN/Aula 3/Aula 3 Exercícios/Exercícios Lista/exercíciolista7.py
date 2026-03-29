# Exercício 7 — Quantidade de caixas de cerâmica (math.ceil())
# Uma caixa de cerâmica cobre 1,5 m². Escreva um programa que leia a área em 
# metros quadrados que o usuário deseja revestir e informe a quantidade mínima de caixas necessárias.

# Exemplo de entrada e saída:
# Digite a área em metros quadrados: 10
# Quantidade de caixas necessárias: 7

import math

áreatotal=float(input('Digite a área (em m²): '))
áreacaixa=1.5
totalcaixas=áreatotal/áreacaixa
qntdcaixas=math.ceil(totalcaixas)

print(f'\nQuantidade de caixas necessárias: {qntdcaixas}')