
import cv2
def emptyimage(img):
    img_1 = cv2.imread(img)
    if img_1 is None:
        res= "Image is empty"
    else:
        res= "Image is not empty"
    return res
img = "ojo2.jpg"
print(emptyimage(img))