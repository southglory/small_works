#https://pythondocs.net/selenium/셀레니움-웹-크롤링-봇-탐지-우회/
#https://selenium-python.readthedocs.io/api.html
import os
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

#내 방식은 "C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Default"로 바로가기 만들고 거기다가 접속하자.
#%USERPROFILE%\AppData\Local\Google\Chrome\User Data 에서 Default, Guest, Profile1, ... 등이 있다. 바로가기 만들고 해당 경로에 ico까지 적용해주면 완벽.

dir = os.path.dirname(os.path.realpath(__file__))
proc = subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="'+dir+'/py_chrometemp"') # 디버거 크롬 구동

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.implicitly_wait(10)

start_url = 'https://quasarzone.com/login?nextUrl=https://quasarzone.com/'
driver.get(start_url)

before_url = driver.current_url
print(before_url)
# 구글 로그인 버튼을 눌러주자. 디폴트 프로필에 의해서 자동 로그인됨.
driver.find_element_by_css_selector('#frm > div > div.mid-btn-area > ul > li:nth-child(4) > a > span').click()
#로그인에 의해서 드라이버의 url이 변하게 될 때까지 최대 30초 기다림.
wait = WebDriverWait(driver, 30) # timeout in seconds -> 30
wait.until(expected_conditions.url_changes(before_url));
print(driver.current_url)


driver.get('https://quasarzone.com/users/attendance')
time.sleep(1)

#퀘XX존 출석체크 가능시간 : 9시~ 24시

now = datetime.now().hour
if now > 9 and now <24:
    try:
        # driver.find_element_by_xpath('//*[@onclick="anttendanceCheck()"]').find_element_by_xpath('..').click()
        driver.find_element_by_xpath('//*[@onclick="anttendanceCheck()"]').click()
    except Exception:
        print("you already check!")  # 이미 출석체크 했으면 콘솔창에 문자열이 나타난다
else:
    print("출석 가능한 시간이 아닙니다.")
    print("퀘XX존 출석체크 가능시간 : 9시~ 24시")
    pass


time.sleep(3)
#크롬드라이버를 닫는다.
driver.close()

#서브프로세스를 완전히 끝낸다.
proc.kill()
try:
    outs, errs = proc.communicate(timeout=15)
except subprocess.TimeoutExpired:
    proc.kill()
    outs, errs = proc.communicate()

os.system('taskkill /f /im chromedriver.exe') #프로세스명을 사용한 프로세스 종료
print("finish")



