from googletrans import Translator
import cv2
import easyocr
import numpy as np
import time
from PIL import ImageFont, ImageDraw, Image

font_path = "NotoSansDevanagari-VariableFont_wdth,wght.ttf"
font = ImageFont.truetype(font_path, 20)



translator=Translator()


reader=easyocr.Reader(['en'],gpu=True)
camera=cv2.VideoCapture(0)
last_ocr_time = 0
ocr_interval = 5
text_display_duration = 3  # Show OCR results for 3 seconds
text_display_start_time = 0
text=[]
while True:
    ret,image=camera.read()
    if not ret:
        break
    
    current_time = time.time()
    if current_time - last_ocr_time >= ocr_interval:
        text = reader.readtext(image)
        last_ocr_time = current_time
        text_display_start_time = current_time

    if current_time - text_display_start_time < text_display_duration:
        image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(image_pil)
        for t in text:
            bbox,lines,score=t
            pts = [tuple(map(int, pt)) for pt in bbox]
            try:
                translate = translator.translate(lines, src='en', dest='hi')
                translated_text = translate.text
            except:
                translated_text = lines
            cv2.polylines(image, [np.array(pts)], isClosed=True, color=(0, 255, 0), thickness=1)
            x, y = pts[0]
            draw.text((x, y - 25), translated_text, font=font, fill=(255, 0, 0))
            print(lines)
            print(translated_text)

        
        
        # Convert back PIL image (with Hindi text) to OpenCV format
    image = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
    cv2.imshow("AR_TRANSLATOR", image)


    key=cv2.waitKey(1)
    if key==27:
        break

camera.release()
cv2.destroyAllWindows()

