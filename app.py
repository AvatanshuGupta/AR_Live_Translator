from googletrans import Translator
import cv2
import easyocr
import matplotlib as plt

reader=easyocr.Reader(['en'],gpu=True)
camera=cv2.VideoCapture(0)
while True:
    ret,image=camera.read()
    cv2.imshow("AR_TRANSLATOR",image)
    text=reader.readtext(image)
    key=cv2.waitKey(1)
    if key==27:
        break

camera.release()
cv2.destroyAllWindows()

