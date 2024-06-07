import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture(1)

detector = PoseDetector(
    staticMode=False,
    modelComplexity=1,
    detectionCon=0.5,
    smoothLandmarks=True,
    enableSegmentation=False,
    smoothSegmentation=True,
    trackCon=0.5,

)

while True:
    rtn, frame = cap.read()

    image = detector.findPose(image)

    lmList, bboxInfo = detector.findPosition(
        image,
        draw=True,
        bboxWithHands=False,

    )

    cv2.imshow('pose', image)

    if cv2.waitKey(1) == ord('q'):
        break


cv2.destroyAllWindows()
