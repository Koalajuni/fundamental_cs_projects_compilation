import easyocr
import cv2
import numpy as np

# 전역변수
pointList = []
gl_areaCut = False
g_carnum = ""

# 이미지 불러와서 전처리
imgFile = './test_data/car2.jpg'
org_image = cv2.imread(imgFile, cv2.IMREAD_COLOR)
gray_image = cv2.imread(imgFile, cv2.IMREAD_GRAYSCALE)


def onChange(pos):
    pass


# 선택한 박스영역을 잘라내서 직사각형의 수평으로 만드는 함수.
def selectBoxCut():
    global g_carnum
    src = np.float32(pointList)
    # 변환할 이미지 크기
    width, height = 300, 80

    # 4가지 지점 (시계방향) - 공간을 시계방향으로
    dst = np.array([
        [0, 0],  # 좌상
        [width, 0],  # 우상
        [width, height],  # 우하
        [0, height],  # 좌하
    ], dtype=np.float32)

    # 영역(Matrix) 변형
    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(org_image, matrix, (width, height))
    result2 = cv2.warpPerspective(binary, matrix, (width, height))

    cv2.imshow('car number org', result)
    cv2.imshow('car numer binary', result2)

    cv2.imwrite('./result/carnum.jpg', result2)

    reader = easyocr.Reader(['en', 'ko'])

    rst = reader.readtext('./result/carnum.jpg')

    for msg in rst:
        print(msg[1])
        g_carnum = msg[1]
        break


# 좌표를 그리는 함수
def pointDraw():
    global gl_areaCut

    tmpImg = org_image.copy()

    i = 0
    for data in pointList:
        cv2.circle(
            tmpImg, data, 10, (0, 0, 255), cv2.FILLED)
        # 라인 그리기
        if i >= 0:
            cv2.line(tmpImg, pointList[i-1], pointList[i],
                     (0, 0, 255), 3, cv2.LINE_AA)

        if i == 3:
            selectBoxCut()

        i += 1

    return tmpImg

# 마우스 제어 함수


def mouse_handler(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        print('오른쪽 버턴 누름')
        pointList.append([x, y])
        print(pointList)
    if event == cv2.EVENT_LBUTTONDOWN:
        print('왼쪽 버턴 누름')
        pointList.pop()
        print(pointList)

    # 드로우로 그림 그리기
    cv2.imshow('org_img', pointDraw())


# 트랙바 만들기
winnames = 'TrackBar'
cv2.namedWindow(winnames)
cv2.imshow('org_img', org_image)
cv2.createTrackbar(
    'threshold',
    winnames,
    127, 255, onChange
)

# 마우스 제어
cv2.setMouseCallback('org_img', mouse_handler)

# 트랙바 제어
while cv2.waitKey(1) != ord('q'):
    pos = cv2.getTrackbarPos('threshold', winnames)
    ret, binary = cv2.threshold(
        gray_image,
        pos, 255, cv2.THRESH_BINARY)
    cv2.imshow(winnames, binary)

    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite('./test_data/car_bin3.jpg', binary)

cv2.destroyAllWindows()
