from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/5.3.4_1/bin/tesseract'

config = ('-l eng --oem 1 --psm 6')

rst = pytesseract.image_to_string(
    Image.open(
        './test_data/news4.jpg'),
    # lang='kor+eng',
    # config=config
)
print(rst)
