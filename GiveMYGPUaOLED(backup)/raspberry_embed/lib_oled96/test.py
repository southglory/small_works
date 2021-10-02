from lib_oled96 import ssd1306
from time import sleep
from PIL import ImageFont, ImageDraw, Image
font = ImageFont.load_default()
import random

from smbus import SMBus                  #  These are the only two variant lines !!
i2cbus = SMBus(1)                        #
# 1 = Raspberry Pi but NOT early REV1 board

episode_1=True
while True:
    oled = ssd1306(i2cbus)
    oled.onoff(0)
    oled.cls()
    sleep(0.5)
    oled.onoff(1)   # Wake it up again. Display contents intact

    draw = oled.canvas   # "draw" onto this canvas, then call display() to send the canvas contents to the hardware.

    # Draw some shapes.
    # First define some constants to allow easy resizing of shapes.
    padding = 2
    shape_width = 20
    top = padding
    bottom = oled.height - padding - 1
    # Draw a rectangle of the same size of screen
    draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)
    # Move left to right keeping track of the current x position for drawing shapes.
    x = padding

    font1 = ImageFont.truetype('FreeSerif.ttf', 15)
    font2 = ImageFont.truetype('FreeSerifItalic.ttf', 17)
    font3 = ImageFont.truetype('FreeSerifItalic.ttf', 37)

    img_dir = '/home/pi/lib_oled96/Luppys/my_selection_final_usage/'
    roses=['rose1a', 'rose1b', 'rose2a', 'rose2b']
    zanmangs_proud= ['proud1', 'proud2', 'proud3']
    zanmangs_poor= ['poor1', 'poor2', 'poor3']
    zanmangs_hello = ['hello1', 'hello2', 'hello3', 'hello4']
    cats_expect= ['expect1', 'expect2']
    cats_happy=['happy1', 'happy2']


    #start!
    draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)
    draw.text((11, 10), 'YK EK', font=font3, fill=1)

    oled.display()
    sleep(2)
    draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)

    # for fun! random sampling.
    now_rose = random.sample(roses,2)
    logo = Image.open(img_dir + now_rose[0]+'.png')
    draw.bitmap((32, 0), logo, fill=1)
    oled.display()
    sleep(1)
    draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)

    logo = Image.open(img_dir + now_rose[1]+'.png')
    draw.bitmap((32, 0), logo, fill=1)
    oled.display()
    sleep(1)
    draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)


    #Zanmang_Loopy!
    draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)
    draw.text((x+3, top), 'Happy !!',  font=font2, fill=1)
    oled.display()
    sleep(2)
        
    draw.text((x+8, top+16), 'zanmang_Loopy', font=font2, fill=1)
    oled.display()
    sleep(1)

    draw.text((x+22, top+40), '& Cats! ^-^', font=font1, fill=1)
    oled.display()
    sleep(1)

    #draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)
    #oled.display()


    while top<65:
        draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)
        draw.text((x+3, top), 'Happy !!',  font=font2, fill=1)   
        draw.text((x+8, top+16), 'zanmang_Loopy', font=font2, fill=1)
        draw.text((x+22, top+40), '& Cats! ^-^', font=font1, fill=1)
        oled.display()
        sleep(0.01)

        #draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)
        #oled.display()
        top += 10
        
    sleep(1)
    oled.cls()


    episode = []
    if episode_1:
        episode.append(random.choice(zanmangs_proud))
        episode.append(random.choice(cats_expect))
        episode.append(random.choice(cats_happy))
    else:
        episode.append(random.choice(zanmangs_poor))
        episode.append(random.choice(zanmangs_hello))
    for scene in episode:
        draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)
        logo = Image.open(img_dir+scene+'.png')     # 이미지 불러오기
        draw.bitmap((0,0), logo, fill=1)         # 이미지 출력 
        oled.display()                                # 화면에 표시하기
        sleep(3)
        
    draw.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)
    final_scene = random.choice(roses)
    logo = Image.open(img_dir+final_scene+'.png')  # 이미지 불러오기
    draw.bitmap((32,0), logo, fill=1)         # 이미지 출력 
    oled.display()                                # 화면에 표시하기
    sleep(3)
 
    oled.cls()
    oled.onoff(0)
    sleep(3)
    episode_1=not(episode_1)