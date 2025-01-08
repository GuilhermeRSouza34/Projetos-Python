valor_em_reais = float(input("Digite o valor em reais (R$): "))
cotacao_dolar = float(input("Digite a cotação do dólar: "))
valor_em_dolares = valor_em_reais / cotacao_dolar
print(f"Com R$ {valor_em_reais}, você pode comprar US$ {valor_em_dolares:.2f}.")
