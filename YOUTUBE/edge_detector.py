import cv2
import numpy as np
#se inciia la video captura el parametro de la función es la camara a utilizar 
cap = cv2.VideoCapture(0)
#se pasan los parametros del espectro de hue segun el color a analizar 
azulBajo = np.array([90,100,20],np.uint8)
azulAlto = np.array([100,255,255],np.uint8)
while True:
  #se leen los frame y ret 
  ret,frame = cap.read()

  if ret==True:
    # se pasa del espacio BGR a HSV 
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV,azulBajo,azulAlto)
    #se obtienen los contornos 
    contornos = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
    #se dibujan los contornos (donde,variable de contornos,todos los contornos,color BGR, grueso del contorno)
    #cv2.drawContours(frame, contornos,-1, (255,0,0), 3)
    for c in contornos:
      area = cv2.contourArea(c) #funcion que calcula el area 
      if area > 3000:
        M = cv2.moments(c) #funcion que detecta el punto central del area 
        #nuevoContorno = cv2.convexHull(c)
        #cv2.drawContours(frame, [nuevoContorno],0, (255,0,0), 3)
        #coordenadas de x y centro
        if (M["m00"]==0): M["m00"]=1 #if para evitar que la divison sea / 0, si es 0 se asigna el valor de 1 
        x = int(M["m10"]/M["m00"]) #formula matematica para calcular area en x 
        y = int(M['m01']/M['m00'])#formula matematica para calcular area en x 
        cv2.circle(frame,(x,y),7,(0,255,0), -1) #se dibuja la forma elegida,(lugar,coordenadas,7 no se que es, BGR, -1 grueso)
        font = cv2.FONT_HERSHEY_SIMPLEX #fuente
        cv2.putText(frame, '{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA) #se dibuja el texto,(frame,valores cambiantes en llaves de x y,fuente,color,grosor,tamaño)
        nuevoContorno = cv2.convexHull(c) #esta funcion suavisa los contornos
        cv2.drawContours(frame, [nuevoContorno], 0, (255,0,0), 3)
    cv2.imshow('maskAzul',mask)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
cap.release()
cv2.destroyAllWindows()