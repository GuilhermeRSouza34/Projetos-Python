#Exemplo basico de erro
print(10 / 0)  # Isso gera uma exceção: ZeroDivisionError

#Estrutura basica de Try e except
try:
    # Código que pode gerar um erro
    numero = int(input("Digite um número: "))
    print(f"O dobro do número é {numero * 2}")
except ValueError:
    # Código executado se o erro ocorrer
    print("Você não digitou um número válido!")
