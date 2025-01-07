numero = int(input("Digite um numero para ver sua tabuada: "))
print("Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")