while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        print(f"Você digitou {numero}")
        break
    except ValueError:
        print("Erro: Você precisa digitar um número válido.")
