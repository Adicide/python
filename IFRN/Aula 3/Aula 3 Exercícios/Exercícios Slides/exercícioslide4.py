# 4. Escreva um programa que tem como entrada um número real representando
# uma quantidade de tempo em horas e que imprime o tempo em horas e
# minutos.

t_horas=float(input('Digite um número no formato "x horas": '))

horas=int(t_horas)
minutos=int((t_horas-horas)*60)

print(f'\n{t_horas}h correspondem a {horas} horas e {minutos} minutos.')