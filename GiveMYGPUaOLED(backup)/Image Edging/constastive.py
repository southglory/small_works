import cv2
import numpy as np

# gray_scale 이미지 불러오기
for ip in range (1,6):
    gray_image = cv2.imread('ori/'+str(ip*2)+'.png', 0) # 인수를 0으로 전달하면 gray 이미지가 로드된다.
    h, w= gray_image.shape

    scale = h/64
    print(gray_image)
    img_binary= gray_image.copy()

    aa = np.array(gray_image)
    AVG = np.mean(aa)
    print(AVG)

    for i in range(0, h):
        for j in range(0,w):
            if gray_image[i,j]> AVG+90:
                img_binary[i, j]=255
            else:
                img_binary[i, j] = 0


    # cv2.imshow('binary_image', img_binary)

    img_result = cv2.resize(img_binary, None, fx=1/scale, fy=1/scale, interpolation = cv2.INTER_AREA)
    cv2.imshow("x0.5 INTER_AREA", img_result)

    # img_result = cv2.resize(gray_image, None, fx=1/scale, fy=1/scale) # cv2.INTER_LINEAR
    # cv2.imshow("x0.5 INTER_LINEAR", img_result)

    cv2.imwrite('ori_result/'+str(ip*2)+'.png', img_result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


