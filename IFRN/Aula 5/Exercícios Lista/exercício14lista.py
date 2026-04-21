# 14. Leia três notas de um aluno. Calcule a média. Se a média for maior ou igual a 5 e menor que 7, exiba "Em recuperação". 

nota1 = float(input('Olá! Insira a sua 1° nota: '))
nota2 = float(input('Ótimo! Agora, coloque a sua 2° nota: '))
nota3 = float(input('Por fim, digite a sua 3° nota: '))
média = (nota1 + nota2 + nota3) / 3 

if 5 <= média < 7:
    print(f'\nSua média: {média:.2f}')
    print('Sua situação: Em recuperação')
elif média >= 7:
    print(f'\nSua média: {média:.2f}')
else: 
    print(f'\nSua média: {média:.2f}')