from TiraFotos import tiraFotos
from Treinamento import algoritmoTreinador
from DeletaRosto import deletaFace
from Reconhecimento import reconhece
from ControleCodigos import controlador

sair = False
while sair != True:
    print()
    print("1. Login")
    print("2. Registro")
    print("3. Deletar registro")
    print()
    print("5. Sair")
    print()

    opcao = int(input("Insira a opção desejada: "))

    if opcao == 1:  #Login
        codigo = int(input("Insira seu código: "))
        reconhece.reconhecimento(codigo)

    elif opcao == 2: #Registro de um novo rosto
        senha = int(input("Insira a senha de adm: "))
        if senha == 1234:
            codigo = controlador.gera_codigo()
            mensagem = "O seu codigo é: " + str(codigo)
            print(mensagem)
            tiraFotos.tiraFoto(codigo)
            algoritmoTreinador.treina_algoritmo(codigo)

    elif opcao == 3:
        senha = int(input("Insira a senha de adm: "))
        if senha == 1234:
            codigo = int(input("Insira o codigo da face que deseja deletar: "))
            deletaFace.deletarFace(codigo)
            

    elif opcao == 5:
        sair = True
