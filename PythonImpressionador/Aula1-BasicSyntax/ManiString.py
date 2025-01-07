palavra = input("Digite uma palavra: ").replace(" ", "").lower()
if palavra == palavra[::-1]:
    print(f"{palavra} é um palíndromo.")
else:
    print(f"{palavra} não é um palíndromo.")
