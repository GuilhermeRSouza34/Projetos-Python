# Exercício 5: Desconto de Produto
# Crie um programa que leia o preço de um produto e calcule o desconto. Se o preço do produto for maior ou igual a 100, o desconto será de 10%. Caso contrário, o desconto será de 5%. Imprima o valor final com o desconto aplicado.

preco = input("Digite o preço do produto: ")
if float(preco) >= 100:
    desconto = float(preco) * 0.10
else:
    desconto = float(preco) * 0.05

valor_final = float(preco) - desconto
print(f"O valor final com desconto é: {valor_final}")
