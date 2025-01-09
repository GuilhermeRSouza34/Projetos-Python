# Exercício 4: Trabalhando com Dicionários
# 1 - Crie um dicionário para armazenar informações de um produto (exemplo: nome, preço, quantidade).
# 2 - Adicione uma nova chave categoria.
# 3 - Atualize o valor da quantidade.
# 4 - Remova a chave categoria.


produto = {"nome": "Notebook", "preco": 4500.00, "quantidade": 10}

# Adicionar categoria
produto["categoria"] = "Informática"

# Atualizar quantidade
produto["quantidade"] = 15

# Remover categoria
produto.pop("categoria")

print(f"Dicionario final: {produto}")
