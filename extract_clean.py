import pytesseract
from PIL import Image

def ocr_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path), lang='eng')
    return text.strip()
