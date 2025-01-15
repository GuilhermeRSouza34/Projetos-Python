compras = ["maçã", "banana", "laranja", "uva"]

try:
    indice = int(input(f"Digite o índice do item (0 a {len(compras) - 1}): "))
    print(f"Você escolheu: {compras[indice]}")
except IndexError:
    print("Erro: Índice fora do intervalo da lista.")
except ValueError:
    print("Erro: Você deve digitar um número inteiro.")
