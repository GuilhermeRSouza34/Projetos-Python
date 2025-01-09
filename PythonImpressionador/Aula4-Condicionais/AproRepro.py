# Exercício 3: Aprovado ou Reprovado
# Crie um programa que leia a nota de um aluno e informe se ele foi aprovado ou reprovado. O aluno será aprovado se a nota for maior ou igual a 7. Se a nota for menor que 7, o aluno será reprovado.

nota = input("Digite a nota do aluno: ")
if float(nota) >= 7:
    print("Aprovado")
elif float(nota) > 3 and float(nota) < 7:
    print("Recuperação")
else:
    print("Reprovado")
    