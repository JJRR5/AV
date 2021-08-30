#HSV HUE SATURATION VALUE HUE(0-179)
import cv2
import numpy as np

cap = cv2.VideoCapture(0) # se incia la videocaptura 0 es la camara

redBajo1 = np.array([100, 100, 20], np.uint8) #parametros para colores bajo 
redAlto1 = np.array([110, 255, 255], np.uint8)# COMPONENTE H VA DE 100 A 110

redBajo2=np.array([120, 100, 20], np.uint8) #parametros para colores en alto 
redAlto2=np.array([130, 255, 255], np.uint8)# COMPONENTE SV VA DE 120 A 130

while True:
  ret,frame = cap.read() #se captura frame por frame
  if ret==True:
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #el frame se pasa de BGR a HSV
    maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1) #se pasan los parametros para el frame con la mascara
    maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
    maskRed = cv2.add(maskRed1, maskRed2) #se crea la mascara fina 
    maskRedvis = cv2.bitwise_and(frame, frame, mask= maskRed)#muestra el color que delimitamos en el color que este es  
    cv2.imshow('frame', frame) 
    cv2.imshow('masKBLUE', maskRed)
    cv2.imshow('maskRedvis', maskRedvis)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
cap.release()
cv2.destroyAllWindows()