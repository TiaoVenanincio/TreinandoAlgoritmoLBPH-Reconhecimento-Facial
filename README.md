# TreinandoAlgoritmoLBPH-Reconhecimento-Facial
Esse projeto é uma tentativa de criar um algoritmo que registra um rosto através da câmera do computador e consegue treinar um algoritmo usando LBPH para diferenciá-lo de outros rostos.

- O conteúdo da pasta TiraFotos é responsável por tirar uma quantidade de fotos do usuário, a qual pode ser definida no código. Tal quantidade de fotos é utilizada para o treinamento do algoritmo.

- O conteúdo da pasta Treinamento é responsável por treinar um algoritmo para o rosto que está sendo cadastrado. A lógica usada é rotular o rosto do usuário como conhecido (1) e outros rostos da subpasta "FacesTreino" como desconhecidos (0). Além disso, nessa pasta ficam salvas as fotos usadas para o treinamento de cada código, como também o algoritmo gerado associado a cada código.

- O conteúdo da pasta ControleCodigos é responsável por gerar, armazenar e ordenar os códigos gerados, mantendo-os em ordem crescente.

- O conteúdo da pasta DeletaRosto é responsável por deletar um rosto registrado. Assim, são apagadas as fotos utilizadas no treinamento, o algoritmo treinado e o código do rosto.

- O conteúdo da pasta Reconhecimento é responsável por buscar o algoritmo do rosto que deseja fazer "Login" através do código fornecido. Em seguida, utiliza-o para verificar se o rosto é conhecido ou desconhecido.

- O conteúdo da pasta ImagensTeste é composto por imagens para testar o algoritmo de reconhecimento através do código '.\Reconhecimento\teste_reconhecimento.py'



* No momento estou atualizando a documentação dos códigos para melhor compreensão.



*Para executar o código, precisa das seguintes bibliotecas instaladas:
    - Opencv, Shutil (operações de arquivo), numpy, Pillow (PIL), os.
