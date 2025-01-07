# Exercício 21
pessoa = {
    "nome": input("Digite o nome: "),
    "idade": int(input("Digite a idade: ")),
    "cidade": input("Digite a cidade: ")
}

print("\nInformações da Pessoa:")
for chave, valor in pessoa.items():
    print(f"{chave.capitalize()}: {valor}")
