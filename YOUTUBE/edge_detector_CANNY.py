import cv2
cartas = cv2.imread("melanoma.jpg")

gris = cv2.cvtColor(cartas,cv2.COLOR_BGR2GRAY)
bordes = cv2.Canny(gris,180,200) #this function detect the edges (image,lowvalue,highvalue)

ctns,_= cv2.findContours(bordes,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(cartas,ctns,-1,(0,255,0),2)
if len(ctns)>=29:
    print("ENFERMEDAD DE PIEL")          
    print("Numero de contornos: ",len(ctns))
    text=("ENFERMEDAD DE PIEL")
else:
    print("SIN ENFERMEDAD")
    text=str(len(ctns))

cv2.putText(cartas,text,(20,20),cv2.FONT_HERSHEY_DUPLEX,0.7,(0,255,0),1)
cv2.imshow("bordes",bordes)
cv2.imshow("cartas",cartas)
cv2.waitKey(0)
cv2.destroyAllWindows()