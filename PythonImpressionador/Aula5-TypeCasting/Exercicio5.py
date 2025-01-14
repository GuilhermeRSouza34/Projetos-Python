entrada = input("Digite um numero inteiro: ")

try:
    numero = int(entrada)
    print(f"Voce digitou o numero inteiro {numero}.")
except ValueError:
    print(f"O valor '{entrada}' não é um número inteiro.")