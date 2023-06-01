import cv2
import os

def tiraFoto(codigo):
    #abre a camera e carrega o detector de faces
    webcam = cv2.VideoCapture(1)
    face_cascade =  cv2.CascadeClassifier('TiraFotos\haarcascade_frontalface_default.xml')
    qtd_foto = 0 #inicia o contador de fotos
    limite = 0  #inicia o contador de frames
    rosto = 0  #qtd de rostos presentes

    #cria o diretorio onde as imagens serao salvas
    diretorio = '.\Treinamento' + '\cod' + str(codigo)
    os.makedirs(diretorio, exist_ok=True)

    #algoritmo para tirar as 50 fotos, com limite de frames (5000)
    while webcam.isOpened() and qtd_foto<50 and limite <5000:
        validacao, frame = webcam.read()
        if not validacao: 
            break
        
        frame = cv2.resize(frame, (640,480)) #frame para trabalhar a deteccao
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converte o frame pra cinza
        faces = face_cascade.detectMultiScale(gray, 1.1, 4) #detecta faces no frame

        salva_frame = 0

        #define um intervalo entre as imagens que serao salvas e verifica se houve reconhecimento no frame anterior
        if limite % 20 == 0 and rosto == 1:
            salva_frame = 1 #caso seja 1, o frame anterior será salvo

        if salva_frame == 1:
            caminho = diretorio + '\Rosto' + str(qtd_foto) + '_' + str(codigo) + '.png'
            cv2.imwrite(caminho, gray) #salva a foto
            qtd_foto += 1
            salva_frame = 0
        
        rosto = 0
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            rosto = 1  #afirma que houve reocnhecimento de rosto

        frame_flip = (cv2.flip(frame,1))
        #escrevendo mensagens no video
        cv2.putText(frame_flip,"REGISTRANDO IMAGENS",(10,25),cv2.QT_FONT_NORMAL,1,255)
        numero_foto = "FOTO " + str(qtd_foto+1)
        cv2.putText(frame_flip,numero_foto,(10,65),cv2.QT_FONT_NORMAL,1,255)
        cv2.imshow("Video da Webcam Invertido", frame_flip)

        if cv2.waitKey(5) == 27: # pressiona esc para sair
            break

        limite += 1

    webcam.release() # encerra a conexão com a webcam
    cv2.destroyAllWindows() # fecha a janela que mostra o que a webcam está vendo

