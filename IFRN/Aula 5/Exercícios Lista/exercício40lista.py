# 40. Leia um caractere e informe se é:

# Uma vogal minúscula (a, e, i, o, u)
# Uma consoante minúscula (qualquer outra letra de a a z)
# Um dígito (0 a 9)
# Outro caractere

caractere = str(input('Digite um caractere: '))

if caractere == 'a' or caractere == 'e' or caractere == 'i' or caractere == 'o' or caractere == 'u':
    print('\nO caractere é uma vogal minúscula.')
elif caractere == 'b' or caractere == 'c' or caractere == 'd' or caractere == 'f' or caractere == 'g' or caractere == 'h' or caractere == 'j' or caractere == 'k' or caractere == 'l' or caractere == 'm' or caractere == 'n' or caractere == 'p' or caractere == 'q' or caractere == 'r' or caractere == 's' or caractere == 't' or caractere == 'v' or caractere == 'w' or caractere == 'x' or caractere == 'y' or caractere == 'z':
    print('\nO caractere é uma consoante minúscula.')
elif '0' <= caractere <= '9':
    print('\nO caractere é um dígito.')
else:
    print('\nOutro caractere.')