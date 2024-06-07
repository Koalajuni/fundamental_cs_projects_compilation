import easyocr

# print(easyocr.__version__)

reader = easyocr.Reader(['en', 'ko'])

rst = reader.readtext('./test_data/news2.jpg')

for msg in rst:
    print(msg[1])

# print(rst)
