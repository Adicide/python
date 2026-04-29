# 45. Leia o número de um mês (1 a 12) e exiba quantos dias ele possui, considerando que o ano é não bissexto. 
# Se o valor for inválido, exiba "Mês inválido".

num_mês = int(input('Digite um número: '))

if num_mês == 1:
    print(f'\nO número {num_mês} é o mês de Janeiro, que tem 31 dias.')
elif num_mês == 2:
    print(f'\nO número {num_mês} é o mês de Fevereiro, que tem 28 dias.')
elif num_mês == 3:
    print(f'\nO número {num_mês} é o mês de Março, que tem 31 dias.')
elif num_mês == 4:
    print(f'\nO número {num_mês} é o mês de Abril, que tem 30 dias.')
elif num_mês == 5:
    print(f'\nO número {num_mês} é o mês de Maio, que tem 31 dias.')
elif num_mês == 6:
    print(f'\nO número {num_mês} é o mês de Junho, que tem 30 dias.')
elif num_mês == 7:
    print(f'\nO número {num_mês} é o mês de Julho, que tem 31 dias.')
elif num_mês == 8:
    print(f'\nO número {num_mês} é o mês de Agosto, que tem 31 dias.')
elif num_mês == 9:
    print(f'\nO número {num_mês} é o mês de Setembro, que tem 30 dias.')
elif num_mês == 10:
    print(f'\nO número {num_mês} é o mês de Outubro, que tem 31 dias.')
elif num_mês == 11:
    print(f'\nO número {num_mês} é o mês de Novembro, que tem 30 dias.')
elif num_mês == 12:
    print(f'\nO número {num_mês} é o mês de Dezembro, que tem 31 dias.')
else:
    print('\nERRO: Mês inválido. Não existe mês maior que o mês 12 (Dezembro).')