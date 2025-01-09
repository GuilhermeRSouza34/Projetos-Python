# Exercício 4: Classificação de Temperatura
# Peça ao usuário para digitar a temperatura em graus Celsius. Se a temperatura for menor que 15°C, o programa deve exibir "Está frio". Se a temperatura estiver entre 15°C e 25°C, o programa deve exibir "Está agradável". Se for maior que 25°C, o programa deve exibir "Está quente".

temperatura = input("Digite a temperatura em graus Celsius: ")

if float(temperatura) < 15:
    print("Está frio")
elif float(temperatura) >= 15 and float(temperatura) <= 25:
    print("Está agradável")
else:
    print("Está quente")

