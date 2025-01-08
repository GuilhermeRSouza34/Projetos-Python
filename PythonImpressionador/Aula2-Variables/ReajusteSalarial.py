salario = float(input("Digite o salario atual: R$"))
aumento = float(input("Digite o percentual de aumento: "))
novo_salario = salario + (salario * aumento / 100)
print(f"O novo salario é R${novo_salario:.2f}.")