import cv2
import numpy as np
#Difference of Gaussian
for p_i in range(1, 6):
    gray = cv2.imread('ori/' + str(2*p_i-1) + '.png', 0)  # 인수를 0으로 전달하면 gray 이미지가 로드된다.
    h, w = gray.shape

    gaussian1 = cv2.GaussianBlur(gray, (5, 5), 1.6)
    gaussian2 = cv2.GaussianBlur(gray, (5, 5), 1)
    DoG = np.zeros_like(gray)
    for i in range(h):
        for j in range(w):
            DoG[i][j] = float(gaussian1[i][j]) - float(gaussian2[i][j])



    # cv2.imshow('DoG', DoG)
    # cv2.waitKey(0)

    cv2.imwrite('DoG_result/' + str(2*p_i-1) + '.png',DoG)
