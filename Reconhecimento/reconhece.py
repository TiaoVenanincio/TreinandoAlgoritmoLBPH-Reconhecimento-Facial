import cv2
import numpy as np
from PIL import Image

def reconhecimento(codigo):
    #abrindo a webcam
    webcam = cv2.VideoCapture(1)

    #preara o haarcascade para verificar a autenticidade apenas se tiver um rosto
    face_cascade =  cv2.CascadeClassifier('TiraFotos\haarcascade_frontalface_default.xml')

    #carrega o algoritmo treinado relacionado ao codigo
    lbph_face_classifier = cv2.face.LBPHFaceRecognizer_create()
    path_algoritmo = '.\Treinamento\AlgoritmosTreinados\cod'+str(codigo)+'\cod'+str(codigo)+'_treinado.xml'
    lbph_face_classifier.read(path_algoritmo)


    limite = 0
    while webcam.isOpened() and limite < 3000:
        validacao, frame = webcam.read()
        if not validacao:
            break
        
        #prepara a imagem para o LPBH treinado
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

        if (rosto == 1) and (limite % 3 == 0):
        #se detecta um rosto, faz o reconhecimento a cada 3 frames
            previsao = lbph_face_classifier.predict(imagem_np)
            rotulo, confiabilidade = previsao

            #determina niveis "aceitaveis" de confiabilidade na detecçao
            if(confiabilidade > 85): 
                rotulo = 0

            if rotulo == 1:
                output = 'Reconhecido' + '   ' + str(confiabilidade)
                print(output)
            else:
                output = 'Desconhecido' + '   ' + str(confiabilidade)
                print(output)

        #O uso do cv2.flip é opcional  
        frame_flip = (cv2.flip(frame,1))
        cv2.imshow("Reconhecendo rosto...", frame_flip)

        if cv2.waitKey(5) == 27: #pressiona esc para sair
            break

        limite += 1
    webcam.release() # encerra a conexão com a webcam
    cv2.destroyAllWindows() # fecha a janela que mostra o que a webcam está vendo