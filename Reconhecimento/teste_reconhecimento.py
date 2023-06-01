import cv2
import os
import numpy as np
from PIL import Image

codigo = 1

#preara o haarcascade para verificar a autenticidade apenas se tiver um rosto
face_cascade =  cv2.CascadeClassifier('TiraFotos\haarcascade_frontalface_default.xml')

#carrega o algoritmo treinado relacionado ao codigo
lbph_face_classifier = cv2.face.LBPHFaceRecognizer_create()
path_algoritmo = '.\Treinamento\AlgoritmosTreinados\cod'+str(codigo)+'\cod'+str(codigo)+'_treinado.xml'
lbph_face_classifier.read(path_algoritmo)

paths = os.listdir('./ImagensTeste/')
for path in paths:  
    caminho = './ImagensTeste/' + path  
    frame = cv2.imread(caminho)
    imagem_resized = cv2.resize(frame, (640,480)) #frame para trabalhar a deteccao
    imagem_pil = Image.fromarray(imagem_resized).convert('L')
    imagem_np = np.array(imagem_pil, 'uint8')

    #detecta as faces na imagem convertida pra cinza
    gray = cv2.cvtColor(imagem_resized, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    rosto = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        rosto = 1 #afirma que um rosto foi reconhecido nesse frame

    if(rosto == 1):
        previsao = lbph_face_classifier.predict(imagem_np)
        rotulo, confiabilidade = previsao

        if(confiabilidade > 75): 
            rotulo = 0

        if rotulo == 1:
            output = 'Reconhecido     ' + path + '   ' + str(confiabilidade)
            print(output)
        else:
            output = 'Desconhecido    ' + path
            print(output)
    else:
        print("Não foi possivel detectar um rosto")
        
    frame_flip = (cv2.flip(frame,1))
    cv2.imshow("Video da Webcam Invertido", frame_flip)

    if cv2.waitKey(1000) == 27: ##pressiona esc para sair
        break

cv2.destroyAllWindows() # fecha a janela que mostra o que a webcam está vendo