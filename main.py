from src import tiraFotos, algoritmoTreinador, deletaFace, reconhece, controlador

sair = False
while sair != True:
    print()
    print("1. Reconhecer rosto registrado")
    print("2. Registrar um novo rosto")
    print("3. Deletar um registro")
    print("4. Registros existentes")
    print()
    print("5. Sair")
    print()

    opcao = int(input("Insira a opção desejada: "))

    if opcao == 1:  #Reconhecer um rosto registrado
        codigo = int(input("Insira seu código: "))
        reconhece.reconhecimento(codigo)

    elif opcao == 2: #Registro de um novo rosto
        codigo = controlador.gera_codigo()
        mensagem = "O seu codigo é: " + str(codigo)
        print(mensagem)
        tiraFotos.tiraFoto(codigo)
        algoritmoTreinador.treina_algoritmo(codigo)

    elif opcao == 3: #Deleta um registro
        codigo = int(input("Insira o codigo da face que deseja deletar: "))
        deletaFace.deletarFace(codigo)
    
    elif opcao == 4: #Imprie os registros existentes
        arquivo = '.\data\codigos.txt'
        try:
            with open(arquivo, 'r') as f:  #abre o arquivo para leitura
                linhas = f.readlines()  #recebe todas as linhas
                if len(linhas) > 0:
                    #cria uma lista com as linhas lidas caso sejam > 0
                    linhas_numeros = [int(linha.strip()) for linha in linhas]

            registros = []
            for numero in linhas_numeros:
                #cria uma lista com os códigos (>0) presentes no arquivo
                if numero > 0:
                    registros.append(numero)
            print("Os códigos já registrados são: %s" % (registros))
        except FileNotFoundError:
            print("Não há registros")

    elif opcao == 5: #Opção de sair do programa
        sair = True
