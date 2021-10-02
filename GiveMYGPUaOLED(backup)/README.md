목표는 컴퓨터 데코레이션을 위해 작은 oled 화면을 데스크탑 내에 연결해놓는 것이다.
전원은 메인보드의 5v에서 받아오면 된다. 아두이노용 oled는 아쉽게도 rgb가 아니라 binary로 출력하는 것 같다. 
따라서 내가 좋아하는 잔망루피 그림 사진을 그대로 쓸 수 없고, 스케치만 따야 한다. 

원래는 포토샵으로 grayscale로 변환, 선명하게, 흐리게 등등 조정한 후,
remove.bg 사이트에서 배경제거 하고 이미지 축소했다.
그런데 배경 제거할 시 선이 없어지는 경우가 많았다.
또한 어떤 경우에는 배경을 제거해주지 못하는 경우도 있다.
선이 조금 없어진 경우는 감안할 수 있지만 아예 배경을 없애주지 못한 경우에는 난감하였다.

목표하는 이미지값이 간단한 디스플레이에 뜨도록 0 혹은 1로 binary되어야 했기 때문이다.
이리 저리 만져보다가 openCv2의 laplacian 필터를 적용해봤다. DoG, LoG, sobel도 적용했다.
놀랍게도 원본 사진을 그대로 넣었을 뿐인데 binary 스케치를 제대로 따줬다.
대박이다.
하지만 완벽하게 하나의 방식이 좋다고 할 수는 없었다.
정답은 없지만, 편하게 알고리즘으로 해결하려고 한다면 laplacian이 제일 무난했고, sobel 과 LoG는 선이 두껍게 잡혀서 파라미터를 잘 조정해서 쓰면 쓸만했다.

remove.bg, 포토샵 등등 헛수고 한 결과물이 무색했다. 그러나 그 결과물이 더 좋게 나온것도 있어서 섞어서 쓰기로 했다.
그렇지만 시간이 많이 걸렸기 때문에 앞으로는 이미지 만질 일 있으면 바로 openCV2로 온다.

laspberry Pi3 : python3, openCV
    powered by 5v gpio port with Computer mainboard's 5v argb port.
mainboard : B550 GAMING CARBON
POWER : Micronics 1050 W

컴퓨터를 켤 때마다 자동으로 라즈베리파이의 코드가 실행되어 oled가 켜진다. 
(자동실행되려면 rc_local 문서 내에 다음을 추가)
python3 /home/pi/... /myImg.py&

(myImg.py와 test.py를 작성하였음.)

![computer with laspberry](https://user-images.githubusercontent.com/51065570/135729015-916bcf98-e5e0-4f17-be44-668b19d7bcd6.jpg)

