import cv2 
import numpy as np 
#draw
def DrawContour(contorno,color):
    for (i,c) in enumerate(contorno):
        M = cv2.moments(c)
        if (M["m00"]==0): M["m00"]==1
        x = int(M["m10"]/M["m00"])
        y = int(M["m01"]/M["m00"])
        cv2.drawContours(imagen,[c],0,color,2)
        cv2.putText(imagen,str(i+1),(x-10,y+10),1,2,(0,0,0),2) #(where,count starts 1,coordinates,,,color,thickness)
    
#Colors
yellowlow= np.array([20,100,20],np.uint8)
yellowhigh= np.array([35,255,255],np.uint8)

violetlow= np.array([120,100,20],np.uint8) #(h,s,v)
violethigh= np.array([150,255,255],np.uint8)

greenlow= np.array([36,100,20],np.uint8) #(h,s,v)
greenhigh= np.array([70,255,255],np.uint8)

redlow1= np.array([0,100,20],np.uint8) #(h,s,v)
redhigh1= np.array([10,255,255],np.uint8)
redlow2= np.array([175,100,20],np.uint8) #(h,s,v)
redhigh2= np.array([180,255,255],np.uint8)

bluelow= np.array([85,100,20],np.uint8) #(h,s,v)
bluehigh= np.array([120,255,255],np.uint8)

imagen = cv2.imread('glaucoma2.jpg')
#Transform the image BGR2HSV
imHSV= cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)
maskyellow = cv2.inRange(imHSV,yellowlow,yellowhigh)
maskviolet = cv2.inRange(imHSV,violetlow,violethigh)
maskgreen = cv2.inRange(imHSV,greenlow,greenhigh)
maskblue = cv2.inRange(imHSV,bluelow,bluehigh)
maskred1 = cv2.inRange(imHSV,redlow1,redhigh1)
maskred2 = cv2.inRange(imHSV,redlow2,redhigh2)
maskred = cv2.add(maskred1,maskred2)

#Finding Contoursxc
contYellow = cv2.findContours(maskyellow,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0] #THIS FUNCTION RETURNS 3 PARAMETERS BUT WE ONLY NEED THE FIRST ONE
contViolet = cv2.findContours(maskviolet,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0] #THIS FUNCTION RETURNS 3 PARAMETERS BUT WE ONLY NEED THE FIRST ONE
contRed = cv2.findContours(maskred,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0] #THIS FUNCTION RETURNS 3 PARAMETERS BUT WE ONLY NEED THE FIRST ONE
contBlue = cv2.findContours(maskblue,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0] #THIS FUNCTION RETURNS 3 PARAMETERS BUT WE ONLY NEED THE FIRST ONE
contGreen = cv2.findContours(maskgreen,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0] #THIS FUNCTION RETURNS 3 PARAMETERS BUT WE ONLY NEED THE FIRST ONE
#DrawContour(contYellow,(0,255,255)) 
#DrawContour(contViolet,(255,0,255)) 
#DrawContour(contRed,(0,0,255)) 
#DrawContour(contBlue,(255,0,0)) 
#DrawContour(contGreen,(0,255,0)) 
#show
#MASK
'''
cv2.imshow("YELLOW",maskyellow)
cv2.imshow("VIOLET",maskviolet)
cv2.imshow("RED",maskred)
cv2.imshow("BLUE",maskblue)
cv2.imshow("GREEN",maskgreen)'''
#ORIGINAL
cv2.imshow("PUNTOS",imagen)
#FINAL_IMAGE
imgfinal = 255*np.ones((250,150,3),dtype=np.uint8)
cv2.circle(imgfinal,(30,30),15,(0,255,255),-1) #(image, center_coordinates, radius, color, thickness)
cv2.circle(imgfinal,(30,70),15,(255,0,255),-1) #(image, center_coordinates, radius, color, thickness)
cv2.circle(imgfinal,(30,110),15,(0,0,255),-1) #(image, center_coordinates, radius, color, thickness)
cv2.circle(imgfinal,(30,150),15,(255,0,0),-1) #(image, center_coordinates, radius, color, thickness)
cv2.circle(imgfinal,(30,190),15,(0,255,0),-1) #(image, center_coordinates, radius, color, thickness)
cv2.putText(imgfinal,"T: ",(30,240),1,2,(0,0,0),2)
cv2.putText(imgfinal,str(len(contYellow)),(65,40),1,2,(0,0,0),2) #(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
cv2.putText(imgfinal,str(len(contViolet)),(65,80),1,2,(0,0,0),2)
cv2.putText(imgfinal,str(len(contRed)),(65,120),1,2,(0,0,0),2)
cv2.putText(imgfinal,str(len(contBlue)),(65,160),1,2,(0,0,0),2)
cv2.putText(imgfinal,str(len(contGreen)),(65,200),1,2,(0,0,0),2)
total = len(contYellow)+len(contViolet)+len(contRed)+len(contBlue)+len(contGreen)
cv2.putText(imgfinal,str(total),(60,240),1,2,(0,0,0),2)
cv2.imshow("FINAL",imgfinal)
cv2.waitKey(0)
cv2.destroyAllWindows()