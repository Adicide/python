# 25. Leia uma temperatura em Celsius. 
# Se for maior que 100, exiba "Acima do ponto de ebulição"; 
# caso contrário, exiba "Abaixo do ponto de ebulição".

temperatura = float(input('Digite a temperatura em °C: '))

if temperatura > 100:
    print('\nTemperatura acima do ponto de ebulição.')
elif temperatura == 100:
    print('\nTemperatura igual ao ponto de ebulição.')
else:
    print('\nTemperatura abaixo do ponto de ebulição.')