# Exercicio 1: Tratamento de exceções ao converter entrada do usuário para inteiro
def exercicio1():
    try:
        numero = int(input("Digite um número: "))
        print(f"Você digitou o número {numero}.")
    except ValueError:
        print("Erro: Você não digitou um número válido.")

# Exercicio 2: Tratamento de exceções ao acessar um índice de uma lista
def exercicio2():
    lista = [1, 2, 3, 4, 5]
    try:
        indice = int(input("Digite um índice para acessar a lista: "))
        print(f"O valor no índice {indice} é {lista[indice]}.")
    except IndexError:
        print("Erro: Índice fora do intervalo da lista.")
    except ValueError:
        print("Erro: Você não digitou um número válido.")

# Exercicio 3: Tratamento de exceções ao abrir um arquivo
def exercicio3():
    try:
        nome_arquivo = input("Digite o nome do arquivo a ser aberto: ")
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except IOError:
        print("Erro: Ocorreu um erro ao ler o arquivo.")

# Exercicio 4: Tratamento de exceções ao dividir dois números
def exercicio4():
    try:
        numerador = int(input("Digite o numerador: "))
        denominador = int(input("Digite o denominador: "))
        resultado = numerador / denominador
        print(f"O resultado da divisão é {resultado}.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except ValueError:
        print("Erro: Você não digitou um número válido.")

# Exercicio 5: Tratamento de exceções ao converter entrada do usuário para float
def exercicio5():
    try:
        numero = float(input("Digite um número decimal: "))
        print(f"Você digitou o número decimal {numero}.")
    except ValueError:
        print("Erro: Você não digitou um número decimal válido.")

# Chame os exercícios para testar
exercicio1()
exercicio2()
exercicio3()
exercicio4()
exercicio5()