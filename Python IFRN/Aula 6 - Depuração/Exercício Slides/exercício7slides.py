# Antes:
# ------------------------
# salario_bruto = float(input("Digite o salário bruto: "))

# inss = salario_bruto * 0.11
# if salario_bruto <= 2000:
# ir = 0
# elif salario_bruto <= 5000:
# ir = salario_bruto * 0.15
# else:
# ir = salario_bruto * 0.275

# salario_liquido = salario_bruto - inss - ir
# print(f"Salario líquido: R$ {salario_liquido :. 2f}")

# Correto:
salario_bruto = float(input("Digite o salário bruto: R$"))

inss = salario_bruto * 0.11
restante = salario_bruto - inss

if salario_bruto <= 2000:
    ir = 0
elif salario_bruto <= 5000:
    ir = restante * 0.15
elif salario_bruto > 5000:
    ir = restante * 0.275

salario_liquido = restante - ir
print(f"Salario líquido: R${salario_liquido:.2f}")