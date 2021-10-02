import cv2
import numpy as np

for p_i in range(1, 6):
    gray_image = cv2.imread('ori/' + str(2*p_i-1) + '.png', 0)  # 인수를 0으로 전달하면 gray 이미지가 로드된다.
    h, w = gray_image.shape
    img_binary= gray_image.copy()

    laplacian = cv2.Laplacian(img_binary, cv2.CV_8U, ksize=5)

    cv2.imwrite('laplacian_result/' + str(2*p_i-1) + '.png', laplacian)
