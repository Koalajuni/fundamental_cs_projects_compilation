import cv2
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(1)

detector = FaceMeshDetector(
    staticMode=False,
    maxFaces=2,
    minDetectionCon=0.5,
    minTrackCon=0.5

)

while True:
    rtn, frame = cap.read()

    img, faces = detector.findFaceMesh(frame, draw=True)
    print(len(faces))

    if faces:
        for face in faces:
            print(face)
            leftEyeUpPoint = face[159]
            leftEyeDownPoint = face[23]

    leftEyeVerticalDistance, info = detector.findDistance(
        leftEyeUpPoint, leftEyeDownPoint
    )

    print(leftEyeVerticalDistance)

    cv2.imshow('window', img)

    if cv2.waitKey(1) == ord('q'):
        break


cv2.destroyAllWindows()
