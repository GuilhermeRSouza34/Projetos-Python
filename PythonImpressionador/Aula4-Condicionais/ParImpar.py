# Exercício 2: Par ou Ímpar
# Peça para o usuário inserir um número inteiro. O programa deve verificar se o número é par ou ímpar. Se for par, imprima "O número é par". Se for ímpar, imprima "O número é ímpar".

numero = input("Digite um número inteiro: ")
if int(numero) % 2 == 0:
    print("O numero é par")
else:
    print("O numero é ímpar")