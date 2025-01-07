try:
    with open("arquivo.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        print(f"Conteúdo do arquivo:\n{''.join(linhas)}")
        print(f"Número de linhas: {len(linhas)}")
except FileNotFoundError:
    print("O arquivo 'arquivo.txt' não foi encontrado.")
