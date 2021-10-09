def LeiaDinheiro(preço):
    valido = False
    while not valido:
        entrada = str(input(preço)).strip()
        if entrada.isalnum():
            print(f'\033[31mERRO! "{entrada}" é um valor inválido\033[m')
        else:
            valido = True
            return entrada