# Exemplo 1
idade = 20
if idade >= 18:
    print("Você é maior de idade")
    
    
    
    
    
# Exemplo 2
idade2 = 15
if idade2 >= 18:
    print("Você é maior de idade")
else:
    print("Você não é maior de idade")
    
    
    
    
# Exemplo 3 utilizando elif
idade3 = 20
if idade3 >= 18:
    print("Você é maior de idade")
elif idade3 < 18:
    print("Você não é um adolecente")
else:
    print("Você é um adulto")
    
    
    
    
# Exemplo 4 Condiçoes compostas utilizando o AND
idade4 = 25
tem_habilitacao = True

if idade4 >= 18 and tem_habilitacao:
    print("Você pode dirigir")
else:
    print("Você não pode dirigir")
    
    
    
    
# Exemplo 4.1 Condiçoes compostas utilizando o OR
idade5 = 25
tem_habilitacao1 = True

if idade5 >= 18 or tem_habilitacao1:
    print("Você pode dirigir")
else:
    print("Você não pode dirigir")
    
    
    
    
# Exemplo 4.2 Condiçoes compostas utilizando o NOT
idade6 = 25
tem_habilitacao2 = True

if not tem_habilitacao2:
    print("Você precisa tirar a habilitacao")
else:
    print("Você pode dirigir")
    
    
    
# Exemplo 5 condicionais em um unico comando
idade7 = 18
status = "Adulto" if idade7 >= 18 else "Menor de idade"
print(f"Você é {status}")