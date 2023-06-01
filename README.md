# TreinandoAlgoritmoLBPH-Reconhecimento-Facial
Esse projeto é uma tentativa de criar um algoritmo que registra um rosto através da câmera do computador e consegue treinar um algoritmo para diferenciá-lo de outros rostos.

- O conteúdo da pasta TiraFotos é responsável por tirar uma quantidade de fotos do usuário, a qual pode ser definida no código. Tal quantidade de fotos é utilizada para o treinamento do algoritmo.

- O conteúdo da pasta Treinamento é responsável por treinar um algoritmo para o rosto que está sendo cadastrado. A lógica usada é rotular o rosto do usuário como conhecido (1) e outros rostos da subpasta "FacesTreino" como desconhecidos (0).

- O conteúdo da pasta ControleCodigos é responsável por gerar, armazenar e ordenar os códigos gerados, mantendo-os em ordem crescente.

- O conteúdo da pasta DeletaRosto é responsável por deletar um rosto registrado. Assim, são apagadas as fotos utilizadas no treinamento, o algoritmo treinado e o código do rosto.

- O conteúdo da pasta Reconhecimento é responsável por buscar o algoritmo do rosto que deseja fazer "Login" através do código fornecido. Em seguida, utiliza-o para verificar se o rosto é conhecido ou desconhecido.


Atualmente estou documentando os códigos para melhor compreensão.