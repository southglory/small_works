import cv2
import numpy as np

for p_i in range(1, 6):
    gray = cv2.imread('ori/' + str(2*p_i-1) + '.png', 0)  # 인수를 0으로 전달하면 gray 이미지가 로드된다.
    h, w = gray.shape

    sobel_x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    sobel_y = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])

    sobel_x = cv2.convertScaleAbs(cv2.filter2D(gray, -1, sobel_x))
    sobel_y = cv2.convertScaleAbs(cv2.filter2D(gray, -1, sobel_y))

    sobel = cv2.addWeighted(sobel_x, 1, sobel_y, 1, 0)
    # cv2.imshow('sobel', sobel)
    # cv2.waitKey(0)

    cv2.imwrite('sobel_result/' + str(2*p_i-1) + '.png', sobel)
