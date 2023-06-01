##Gerado através de IA com pequenas alterações
def gera_codigo():
    arquivo = '.\ControleCodigos\codigos.txt'
    try:
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
            if len(linhas) > 0:
                linhas_numeros = [int(linha.strip()) for linha in linhas]
                if 0 in linhas_numeros:
                    sequencia = set(range(1, len(linhas) + 2))
                    numeros_existentes = set(linhas_numeros)
                    novo_codigo = min(sequencia - numeros_existentes)
                    linhas_numeros[linhas_numeros.index(0)] = novo_codigo
                    linhas = [str(num) + '\n' for num in linhas_numeros]
            else:
                novo_codigo = 1
                linhas = [str(novo_codigo) + '\n']
    except FileNotFoundError:
        novo_codigo = 1
        linhas = [str(novo_codigo) + '\n']

    with open(arquivo, 'w') as f:
        f.writelines(linhas)

    return novo_codigo

def apagar_codigo(codigo):
    arquivo = '.\ControleCodigos\codigos.txt'
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    with open(arquivo, 'w') as f:
        for linha in linhas:
            if linha.strip() != str(codigo):
                f.write(linha)
            else:
                f.write('0\n')



