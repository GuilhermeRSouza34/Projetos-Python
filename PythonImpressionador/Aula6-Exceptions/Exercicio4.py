def valida_idade(idade):
    if idade < 18:
        raise ValueError("Você precisa ter pelo menos 18 anos.")

try:
    idade = int(input("Digite sua idade: "))
    valida_idade(idade)
    print("Idade válida.")
except ValueError as e:
    print(f"Erro: {e}")
