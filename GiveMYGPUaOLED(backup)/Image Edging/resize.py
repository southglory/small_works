import cv2
import numpy as np

for p_i in range(1, 6):
    gray_image = cv2.imread('DoG_result/' + str(2*p_i-1) + '.png', 0)  # 인수를 0으로 전달하면 gray 이미지가 로드된다.
    h, w= gray_image.shape
    scale = h/64

    img_resized = cv2.resize(gray_image, None, fx=1 / scale, fy=1 / scale, interpolation=cv2.INTER_AREA)
    # cv2.imshow("x0.5 INTER_AREA", img_resized)

    cv2.imwrite('DoG_result/resize/' + str(2*p_i-1) + '.png', img_resized)
