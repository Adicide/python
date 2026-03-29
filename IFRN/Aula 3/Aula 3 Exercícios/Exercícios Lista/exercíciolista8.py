# Exercício 8 — Tempo em horas e minutos (math.floor())
# Escreva um programa que leia uma quantidade de tempo em horas (número real) 
# e imprima o tempo separado em horas inteiras e minutos.

# Exemplo de entrada e saída:
# Digite o tempo em horas: 2.5
# Tempo: 2 hora(s) e 30 minuto(s)

import math

tempo_h = float(input('Digite o tempo em horas (ex: 2.5): '))
horas = int(tempo_h)
minutos = int((tempo_h-horas)*60)

print(f'\n{tempo_h} h correspondem a {horas} h e {minutos} min.')