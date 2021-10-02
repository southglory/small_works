import cv2
import numpy as np


dir_name = "LoG_result"

for p_i in range(1, 6):
    gray_image = cv2.imread(dir_name + '/resize/' + str(2*p_i-1) + '.png', 0)  # 인수를 0으로 전달하면 gray 이미지가 로드된다.
    h, w = gray_image.shape
    img_binary= gray_image.copy()

    for i in range(0, h):
        for j in range(0,w):
            if gray_image[i,j]> 3: #방식마다 다름
                img_binary[i, j]=255
            else:
                img_binary[i, j] = 0

    cv2.imwrite('Bitwise_results/'+dir_name +'_resized/'+ str(2*p_i-1) + '.png', img_binary)
