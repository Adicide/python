# 42. Leia o número de um trimestre (1 a 4) e exiba os meses correspondentes:

# Trimestre 1: "Janeiro, Fevereiro, Março"
# Trimestre 2: "Abril, Maio, Junho"
# Trimestre 3: "Julho, Agosto, Setembro"
# Trimestre 4: "Outubro, Novembro, Dezembro"
# Outro valor: "Trimestre inválido"

trimestre = int(input('Insira o número do trimestre (de 1 a 4): '))

if trimestre == 1:
    print('\nMeses: Janeiro, Fevereiro e Março.')
elif trimestre == 2:
    print('\nMeses: Abril, Maio e Junho.')
elif trimestre == 3:
    print('\nMeses: Julho, Agosto e Setembro.')
elif trimestre == 4:
    print('\nMeses: Outubro, Novembro e Dezembro.')
else:
    print('\nTrimestre inválido.')