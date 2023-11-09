##Gerado através de IA com pequenas alterações
def gera_codigo():
    arquivo = '.\data\codigos.txt'
    try:
        with open(arquivo, 'r') as f:  #abre o arquivo para leitura
            linhas = f.readlines()  #recebe todas as linhas
            if len(linhas) > 0:
                #cria uma lista com as linhas lidas caso sejam > 0
                linhas_numeros = [int(linha.strip()) for linha in linhas]
                if 0 in linhas_numeros:
                    #Se há 0, talvez seja um espaço entre dois codigos onde havia um anterior
                    #Por exemplo 1, 0, 3, onde o codigo 2 foi apagado

                    #Cria uma sequencia do tamanho da lista, começando pelo 1
                    sequencia = set(range(1, len(linhas) + 2))
                    #cria um conjunto dos numeros existentes
                    numeros_existentes = set(linhas_numeros)
                    #encontra o menor numero que nao está presente nos codigos
                    novo_codigo = min(sequencia - numeros_existentes)
                    #substitui o primeiro 0 pelo menor numero não presente anteriormente
                    linhas_numeros[linhas_numeros.index(0)] = novo_codigo
                    #atualiza a lista com os numeros
                    linhas = [str(num) + '\n' for num in linhas_numeros]
            else:
            #caso nao haja linhas no arquivo
                #começa pelo 1
                novo_codigo = 1
                linhas = [str(novo_codigo) + '\n']
    except FileNotFoundError:
    #caso nao exista o diretorio, o codigo será 1
        novo_codigo = 1
        linhas = [str(novo_codigo) + '\n']

    with open(arquivo, 'w') as f:
    #abre em modo escrita e coloca os codigos atualizados no arquivo
        f.writelines(linhas)

    return novo_codigo

def apagar_codigo(codigo):
    arquivo = '.\data\codigos.txt'
    with open(arquivo, 'r') as f:
    #abre em modo de leitura, pega as linhas existentes
        linhas = f.readlines()

    with open(arquivo, 'w') as f:
    #abre para escrita
        #usa as linhas obtidas anteriormente
        for linha in linhas:
            if linha.strip() != str(codigo):
            #compara as linhas, as que são diferentes do codigo sao escritas novamente
                f.write(linha)
            else:
            #a linha igual ao codigo que sera apagado é substituida por 0
                f.write('0\n')



