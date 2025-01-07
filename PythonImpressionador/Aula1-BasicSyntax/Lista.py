numeros = []
for i in range(5):
    num = float(input(f"Digite o {i+1}º numero: "))
    numeros.append(num)

print(f"Lista: {numeros}")
print(f"Maior número: {max(numeros)}")
print(f"Menor número: {min(numeros)}")
print(f"Soma dos números: {sum(numeros)}")