import cv2
from cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

cap = cv2.VideoCapture(1)

segmentor = SelfiSegmentation(model=0)

while True:
    rtn, frame = cap.read()

    imageOut = segmentor.removeBG(frame, imgBg=(255, 0, 255), cutThreshold=0.1)

    cv2.imshow('Seg', imageOut)

    if cv2.waitKey(1) == ord('q'):
        break


cv2.destroyAllWindows()
