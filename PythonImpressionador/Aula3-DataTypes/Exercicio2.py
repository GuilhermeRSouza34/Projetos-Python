# Exercício 2: Trabalhando com Strings
# 1 - Crie uma variável com seu nome.
# 2 - Converta todo o texto para maiúsculas.
# 3 - Divida o nome em caracteres individuais.
# 4 - Use o método .replace() para substituir uma letra por outra.


nome = "Guilherme"

# Converter para maiúsculas
nome_maiusculo = print(nome.upper())

# Dividir em caracteres
caracteres = print(nome.split())

# Substituir uma letra
novo_nome = print(nome.replace("G", "J"))

print(f"Nome original: {nome}")
print(f"Maiúsculas: {nome_maiusculo}")
print(f"Caracteres: {caracteres}")
print(f"Novo nome: {novo_nome}")
