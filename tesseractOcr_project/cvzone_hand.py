import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(1)

detector = HandDetector(
    staticMode=False,
    maxHands=2,
    modelComplexity=1,
    detectionCon=0.5,
    minTrackCon=0.5,

)

while True:
    rtn, frame = cap.read()

    hands, image = detector.findHands(frame, draw=True, flipType=True)

    if hands:
        for hand in hands:
            # print(hand)
            handpoint = hand["lmList"]

            point4 = handpoint[4]
            point8 = handpoint[8]
            print(point4, point8)

            length, info, image = detector.findDistance(
                point4[:2], point8[:2], image, color=(0, 0, 255), scale=10,
            )

    cv2.imshow('window', image)

    if cv2.waitKey(1) == ord('q'):
        break


cv2.destroyAllWindows()
