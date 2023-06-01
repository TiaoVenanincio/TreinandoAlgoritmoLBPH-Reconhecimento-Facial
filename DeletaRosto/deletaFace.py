import shutil
from ControleCodigos import controlador

def deletarFace(codigo):
    #apaga as imagens associadas ao codigo
    try:
        diretorio = '.\Treinamento' + '\cod' + str(codigo)
        shutil.rmtree(diretorio)
        print()
        print("Diretorio de faces apagado")
    except:
        print()
        print("Diretório de faces inexistente")

    #apaga o algoritmo treinado
    try:
        diretorio_algoritmo = '.\Treinamento\AlgoritmosTreinados\cod' + str(codigo)
        shutil.rmtree(diretorio_algoritmo)
        print()
        print("Diretorio de algoritmos apagado")
    except:
        print("Diretório de algoritmos inexistente")

    
    #apaga o codigo na lista
    controlador.apagar_codigo(codigo)