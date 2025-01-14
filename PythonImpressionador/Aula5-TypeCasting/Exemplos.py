# EXEMPLO 1 - CONVERSÃO IMPLÍCITA
inteiro = 10
decimal = 2.5
soma = inteiro + decimal
print(soma) # Resposta vai ser: 12.5 (float)

# EXEMPLO 2 - CONVERSÃO EXPLÍCITA
texto = "50"
numero = int(texto)
print(numero) # Resposta vai ser: 50 (int)

# EXEMPLO 3 - MISTURA DE TIPOS
inteiro2 = 10
float_para_int = int(4.9)
resultado2 = inteiro2 + float_para_int
print(resultado2) # Resposta vai ser: 14 (int)