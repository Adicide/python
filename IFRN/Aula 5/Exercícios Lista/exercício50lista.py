# 50. Crie um mini menu de uma lanchonete. Leia a opção escolhida:

# 1 — Hambúrguer: R$ 18,00
# 2 — Hot-dog: R$ 12,00
# 3 — Suco: R$ 8,00
# 4 — Refrigerante: R$ 6,00
# 5 — Sair sem pedir
# Leia a quantidade desejada para a opção escolhida e exiba o total a pagar. 
# Se a opção for inválida, exiba "Opção inválida".


print('*** MENU ***''\n1 — Hambúrguer: R$ 18,00''\n2 — Hot-dog: R$ 12,00''\n3 — Suco: R$ 8,00''\n4 — Refrigerante: R$ 6,00''\n5 — Sair sem pedir')
opção = int(input('\nEscolha uma opção: '))

if opção == 5:
    print('\nSaindo do menu... Até a próxima!')
else:
    if opção == 1:
        quantidade = int(input('Qual a quantidade? '))
        valor = quantidade * 18
        print(f'\nValor total: R${valor:.2f}')
        
    elif opção == 2:
        quantidade = int(input('Qual a quantidade? '))
        valor = quantidade * 12
        print(f'\nValor total: R${valor:.2f}')
        
    elif opção == 3:
        quantidade = int(input('Qual a quantidade? '))
        valor = quantidade * 8
        print(f'\nValor total: R${valor:.2f}')
        
    elif opção == 4:
        quantidade = int(input('Qual a quantidade? '))
        valor = quantidade * 6
        print(f'\nValor total: R${valor:.2f}')
        
    else:
        print('ERRO: Opção inválida!')