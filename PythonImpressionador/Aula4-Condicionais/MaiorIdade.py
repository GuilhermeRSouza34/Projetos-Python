#Exercício 1: Maioridade
#Crie um programa que leia a idade de uma pessoa e imprima se ela é maior ou menor de idade. Se a pessoa for maior de idade, exiba "Você é maior de idade!". Caso contrário, exiba "Você é menor de idade!".

idade = input("Digite sua idade: ")
if int(idade) >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
