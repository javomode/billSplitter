import glob
import pytesseract

img = glob.glob('invoices_images/*.jpg')

for i, image in enumerate(img):
    text = pytesseract.image_to_string(image, lang='eng')
    print(text)
