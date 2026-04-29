# 50. Escreva um programa que exibe a seguinte tabela de conversão de temperaturas de 0 °C a 100 °C, 
# de 10 em 10 graus, mostrando Celsius, Fahrenheit e Kelvin. 
# Ao lado de cada linha, classifique a temperatura como 
# "fria" (< 15 °C), "agradável" (15 °C a 25 °C) ou "quente" (> 25 °C).

# Fórmulas: F = C × 9/5 + 32 ; K = C + 273.15

print(f'{"Celsius":<8}\t{"Fahrenheit":<8}\t{"Kelvin":<8}\t{"Classificação":<8}')

c = 0
while c <= 100:
    f = c * 9/5 + 32
    k = c + 273.15
    if c < 15:
        classificação = 'Fria'
    elif 15 <= c <= 25:
        classificação = 'Agradável' 
    elif c > 25:
        classificação = 'Quente'

    print(f'{c:^8}\t{f:^8}\t{k:^8}\t{classificação:^8}')
    c += 10