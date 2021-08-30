import cv2
import numpy as np  

#this line creates a white window 
imagen = 255*np.ones((600,600,3),dtype=np.uint8)

#drawing a line 
cv2.line(imagen,(0,0),(600,100),(255,0,0),10)

#drawing a rectangle
cv2.rectangle(imagen,(1,1),(600,600),(0,255,0),5) #(imagen,firstpoint,final,point,color,thickness)

#drawing a circle
cv2.circle(imagen,(300,300),100,(100,15,0),-1)#(imagen,centerpoint,radio,color, thickness)
#note: if you use -1 in the final parameter the figure will be filling

font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(imagen,"PRACTICANDO JEJE",(10,30),font,5,(0,100,150),2,cv2.LINE_AA)
#(imagen,text,position,font,size,color,thickness,linetype)

cv2.imshow("IMAGEN",imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

