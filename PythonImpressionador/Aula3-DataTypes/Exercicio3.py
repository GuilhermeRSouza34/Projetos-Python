# Exercício 3: Manipulando Listas
#1 - Crie uma lista com 5 números.
#2 - Adicione dois números à lista.
#3 - Remova o terceiro número.
#4 - Ordene a lista em ordem decrescente.


numeros = [1, 2, 3, 4, 5]

# Adicionar dois números
numeros.append(6)
numeros.append(7)

# Remover o terceiro número
numeros.remove(3)  # Complete aqui

# Ordenar em ordem decrescente
numeros.sort(reverse=True)

print(f"Lista final: {numeros}")
