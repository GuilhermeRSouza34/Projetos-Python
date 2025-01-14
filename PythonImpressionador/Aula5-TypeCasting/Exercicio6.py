numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

numero1 = float(numero1)
numero2 = float(numero2)

if numero1 > numero2:
    print(f"O número {numero1} é maior que {numero2}.")
elif numero1 < numero2:
    print(f"O número {numero2} é maior que {numero1}.")
else:
    print(f"Os números são iguais: {numero1}.")
