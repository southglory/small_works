#https://pythondocs.net/selenium/셀레니움-웹-크롤링-봇-탐지-우회/
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil

#내 방식은 "C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Default"로 바로가기 만들고 거기다가 접속하자.
#%USERPROFILE%\AppData\Local\Google\Chrome\User Data 에서 Default, Guest, Profile1, ... 등이 있다. 바로가기 만들고 해당 경로에 ico까지 적용해주면 완벽.

# try:
#     shutil.rmtree(r"c:\py_chrometemp")  #쿠키 / 캐쉬파일 삭제
# except FileNotFoundError:
#     pass

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\py_chrometemp"') # 디버거 크롬 구동


option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.implicitly_wait(10)


#위 코드 블록 가져다가 쓰면 됨.
driver.close()