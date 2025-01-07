import random

numero_secreto = random.randint(1, 50)
tentativas = 5

print("Bem vindo ao jogo de Adivinhação!")
print("Escolha um número entre 1 e 50.")
while tentativas > 0:
    chute = int(input("Qual o seu palpite: "))
    if chute == numero_secreto:
        print("Parabéns, você acertou!")
        break
    elif chute < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")
    tentativas -= 1
    
if tentativas == 0:
    print(f"Você perdeu! O número secreto era {numero_secreto}.")