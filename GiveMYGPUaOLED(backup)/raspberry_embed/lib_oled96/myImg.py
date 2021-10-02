from PIL import Image, ImageDraw, ImageFont
from lib_oled96 import ssd1306
from time import sleep
from smbus import SMBus

i2cbus = SMBus(1)
oled = ssd1306(i2cbus)
draw = oled.canvas
sleep(3)
oled.cls() 

for i in range(1, 6):
    sleep(0.5)
    oled.onoff(1)   # Wake it up again. Display contents intact
    
    logo = Image.open('/home/pi/lib_oled96/Luppys/laplacian_result/resize/'+str(2*i-1)+'.png')     # 이미지 불러오기
    draw.bitmap((0,0), logo, fill=1)         # 이미지 출력 
    oled.display()                                # 화면에 표시하기
    sleep(3)

    oled.onoff(0)   # kill the oled.  RAM contents still there.
    oled.cls() 

