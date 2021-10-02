import cv2
import numpy as np
#laplacian of gaussian
for p_i in range(1, 6):
    gray = cv2.imread('ori/' + str(2*p_i-1) + '.png', 0)  # 인수를 0으로 전달하면 gray 이미지가 로드된다.
    h, w = gray.shape

    mask3 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    gaussian = cv2.GaussianBlur(gray, (5, 5), 0)
    LoG = cv2.filter2D(gaussian, -1, mask3)
    gaussian = cv2.GaussianBlur(gray, (5, 5), 0)
    LoG = cv2.filter2D(gaussian, -1, mask3)


    # cv2.imshow('LoG', LoG.astype(float))
    # cv2.waitKey(0)

    cv2.imwrite('LoG_result/' + str(2*p_i-1) + '.png',LoG.astype(float))
