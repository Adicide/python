# 5. Escreva um programa que tem como entrada um valor de área em metros
# quadrados e que informa a quantidade de caixas de cerâmica necessárias
# para revestir a área informada, sabendo que uma caixa contém 1,5 m2 de
# cerâmica.

import math

áreatotal=float(input('Digite o valor da área (m²): '))

área_pcaixa=1.5
caixas= áreatotal/área_pcaixa
qntdcaixas = math.ceil(caixas)

print(f'\nA quantidade de caixas necessárias é: {qntdcaixas}')