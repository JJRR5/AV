import cv2
import numpy as np 

def draw(mask,color):
    contornos = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
    #se dibujan los contornos (donde,variable de contornos,todos los contornos,color BGR, grueso del contorno)
    #cv2.drawContours(frame, contornos,-1, (255,0,0), 3)
    for c in contornos:
        area = cv2.contourArea(c) #funcion que calcula el area 
        if area > 3000:
            x,y,w,h = cv2.boundingRect(c)
            if color == (255,0,0): 
                cv2.rectangle(frame,(x,y),(x+w,y+h),color,3)
                cv2.line(frame,(x,y),(x+w,y+h),color,3)
                cv2.line(frame,(x+w,y),(x,y+h),color,3)
                cv2.putText(frame,'BLUE',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
            if color == (0,255,255):
                M=cv2.moments(c)
                if (M["m00"]==0):M["m00"]==1
                xcentro = int(M["m10"]/M["m00"])
                ycentro = int(M["m01"]/M["m00"])
                radio=xcentro-x 
                cv2.circle(frame,(xcentro,ycentro),radio,color,3)
                cv2.putText(frame,"YELLOW",(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
            if color == (0,0,255): 
                cv2.rectangle(frame,(x,y),(x+w,y+h),color,3)
                cv2.line(frame,(x,y),(x+w,y+h),color,3)
                cv2.line(frame,(x+w,y),(x,y+h),color,3)
                cv2.putText(frame,'RED',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
            if color == (0,255,0): 
                cv2.rectangle(frame,(x,y),(x+w,y+h),color,3)
                cv2.line(frame,(x,y),(x+w,y+h),color,3)
                cv2.line(frame,(x+w,y),(x,y+h),color,3)
                cv2.putText(frame,'GREEN',(x-10,y-10),font,0.75,color,2,cv2.LINE_AA)
            '''
            M = cv2.moments(c) #funcion que detecta el punto central del area 
            if (M["m00"]==0): M["m00"]=1 #if para evitar que la divison sea / 0, si es 0 se asigna el valor de 1 
            x = int(M["m10"]/M["m00"]) #formula matematica para calcular area en x 
            y = int(M['m01']/M['m00'])#formula matematica para calcular area en x 
            nuevoContorno = cv2.convexHull(c) #esta funcion suavisa los contornos
            cv2.circle(frame,(x,y),7,(0,255,0), -1) #se dibuja la forma elegida,(lugar,coordenadas,7 no se que es, BGR, -1 grueso)
            cv2.putText(frame, '{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA) #se dibuja el texto,(frame,valores cambiantes en llaves de x y,fuente,color,grosor,tamaño)
            cv2.drawContours(frame, [nuevoContorno], 0,color, 3)
            '''
            

cap = cv2.VideoCapture(0)

#delimitar colores 
bluelow = np.array([90,100,20],np.uint8)
bluehigh = np.array([100,255,255],np.uint8)

greenlow = np.array([45,100,20],np.uint8)
greenhigh = np.array([65,255,255],np.uint8)

yellowlow = np.array([15,100,20],np.uint8)
yellowhigh = np.array([45,255,255],np.uint8)

redlow1 = np.array([0,100,20],np.uint8)
redhigh1 = np.array([5,255,255],np.uint8)
redlow2 = np.array([175,100,20],np.uint8)
redhigh2 = np.array([179,255,255],np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX #fuente
while True:
    ret,frame = cap.read()
    if ret==True:
        frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        maskBlue = cv2.inRange(frameHSV,bluelow,bluehigh)
        maskYellow = cv2.inRange(frameHSV,yellowlow,yellowhigh)
        maskGreen= cv2.inRange(frameHSV,greenlow,greenhigh)
        maskRed1= cv2.inRange(frameHSV,redlow1,redhigh1)
        maskRed2 = cv2.inRange(frameHSV,redlow2,redhigh2)
        maskRed= cv2.add(maskRed1,maskRed2)
        draw(maskBlue,(255,0,0))
        draw(maskGreen,(0,255,0))
        draw(maskRed,(0,0,255))
        draw(maskYellow,(0,255,255))
        cv2.imshow('FRAME',frame)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break
cap.release()
cv2.destroyAllWindows()
        
        




