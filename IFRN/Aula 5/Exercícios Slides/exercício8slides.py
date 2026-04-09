idade_nadador=int(input('\nBem-vindo, nadador! Digite a sua idade: '))

if 5 <= idade_nadador <= 7:
    print('\nSua categoria é: Peixinho\n')

if 8 <= idade_nadador <= 10:
    print('\nSua categoria é: Infantil A\n')

if 11 <= idade_nadador <= 13:
    print('\nSua categoria é: Infantil B\n')

if 14 <= idade_nadador <= 17:
    print('\nSua categoria é: Juvenil\n')

if idade_nadador >= 18:
    print('\nSua categoria é: Adulto\n')