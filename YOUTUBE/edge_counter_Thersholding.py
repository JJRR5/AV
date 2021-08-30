import cv2
imagen =cv2.imread('piel.jpg')
gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
_,th = cv2.threshold(gris,240,255,cv2.THRESH_BINARY_INV) #(img in gray, umbral in pixels(2),see the result)

cont,_ = cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #function that find the contours of the objects,with three parameters
'''
cv2.drawContours(imagen,cont,-1,(0,0,255),2) #(img,contours,all of them,color,thickness)
print("CONTORNOS: ",len(cont))
cv2.imshow('coins',imagen)
cv2.imshow('th',th)
'''
font = cv2.FONT_HERSHEY_COMPLEX
i=0
for c in cont:
    M = cv2.moments(c)
    if (M["m00"]==0): M["m00"]=1
    x=int(M["m10"]/M["m00"])
    y=int(M["m01"]/M["m00"])
    
    mensaje = 'Num :' + str(i+1)
    cv2.putText(imagen,mensaje,(x-40,y),font,0.75,(255,0,0),2,cv2.LINE_AA)
    cv2.drawContours(imagen,[c],-1,(0,0,255),2)
    cv2.imshow('ORIGINAL',imagen)
    cv2.waitKey(0)
    i = i+1
cv2.destroyAllWindows()