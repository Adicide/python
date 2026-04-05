# 6. Python permite encadear operadores relacionais como açúcar sintático. 
# As duas expressões abaixo são equivalentes?

# A < B and B > C
# A < B > C

# Execute as duas no interpretador e compare os resultados. São equivalentes? Por quê?

A=4
B=10
C=4

print(A<B and B>C)
print(A<B>C)

# Resultado: Os dois são equivalentes, pois, em ambos resultados, B é maior que A e C.