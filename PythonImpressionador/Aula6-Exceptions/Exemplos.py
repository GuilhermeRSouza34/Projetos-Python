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


#Lidando com multiplos exceções
try:
    numero2 = int(input("Digite um número: "))
    resultado2 = 10 / numero2
    print(f"Resultado: {resultado2}")
except ValueError:
    print("Erro: Você precisa digitar um número.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")


#Utilizando blocos else e finally
try:
    numero3 = int(input("Digite um número: "))
    print(f"Você digitou {numero3}")
except ValueError:
    print("Erro: Entrada inválida.")
else:
    print("Nenhum erro ocorreu.")
finally:
    print("Fim do programa!")
