import os
import cv2
import numpy as np

#carrega o detector de faces
face_cascade =  cv2.CascadeClassifier('.\data\haarcascade_frontalface_default.xml')

def extrai_caracteristicas(imagem, lbph_labels, lbph_faces, label):
    #detecta faces na imagem
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    faces_detectadas = face_cascade.detectMultiScale(imagem_cinza, 1.1, 4)
     #Extrai as características das faces detectadas
    for(x, y, w, h) in faces_detectadas:
        #aumentando o tamanho do retangulo:
        y = int(y-y*0.1) #aumenta o tamanho da altura na parte de cima
        yh = int((y+h)*1.15) #aumenta o tamanho da altura na parte de baixo
        roi = imagem_cinza[y:yh, x:x+w] #recorta a imagem
        lbph_labels.append(label)
        lbph_faces.append(roi)

def treina_algoritmo(codigo):
    #Cria um objeto classificador LBPH
    lbph = cv2.face.LBPHFaceRecognizer_create()

    #Define os parâmetros do LBPH
    lbph.setGridX(5)  # Define o tamanho do bloco (padrão: 8)
    lbph.setGridY(5)
    lbph.setNeighbors(12)  # Define o número de vizinhos (padrão: 8)

    #inicializando listas para rotulos e faces
    lbph_labels = []
    lbph_faces = []

    #diretorio das imagens p/ treinamento
    rostos_conhecidos = '.\data\Faces_conhecidas\cod' + str(codigo)
    # Percorre as imagens do rosto conhecido
    for arquivo in os.listdir(rostos_conhecidos):
        caminho_arquivo = os.path.join(rostos_conhecidos, arquivo)
        imagem = cv2.imread(caminho_arquivo)
        extrai_caracteristicas(imagem, lbph_labels, lbph_faces, 1)

    #diretorio das imagens p/ treinamento
    rostos_desconhecidos = '.\data\Faces_desconhecidas'
    # Percorre as imagens dos outros rostos
    for arquivo in os.listdir(rostos_desconhecidos):
        caminho_arquivo = os.path.join(rostos_desconhecidos, arquivo)
        imagem = cv2.imread(caminho_arquivo)
        extrai_caracteristicas(imagem, lbph_labels, lbph_faces, 0)

    #treina o classificador pelos rotulos
    lbph.train(lbph_faces, np.array(lbph_labels))

    path = '.\data\Algoritmos_treinados\cod' + str(codigo)
    #cria o diretorio
    os.makedirs(path, exist_ok=True)
    
    # Salva o classificador treinado no diretorio criado acima
    caminho = '.\data\Algoritmos_treinados\cod'+ str(codigo)+ '\cod' + str(codigo) + '_treinado.xml'
    lbph.save(caminho)