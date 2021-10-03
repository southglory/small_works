import os, subprocess
print(os.system('tasklist'))

#os.system('taskkill /f /pid 11172') #pid를 사용한 프로세스 종료
# os.system('taskkill /f /im chromedriver.exe') #프로세스명을 사용한 프로세스 종료

##---------------------------------------------------------##
#http://daplus.net/python-shell-true%EB%A1%9C-%EC%8B%9C%EC%9E%91%EB%90%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%84%9C%EB%B8%8C-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4%EB%A5%BC-%EC%A2%85%EB%A3%8C%ED%95%98%EB%8A%94-%EB%B0%A9/
#     다음은 제때제떄 subprocess를 종료하는 방법
#
# 제대로 작동하는 응용 프로그램을 올바르게 정리하려면 자식 프로세스를 종료하고 통신을 완료해야합니다
# proc = subprocess.Popen(...)
# try:
#     outs, errs = proc.communicate(timeout=15)
# except subprocess.TimeoutExpired:
#     proc.kill()
#     outs, errs = proc.communicate()
# 근데 안먹는다 ㅎㅎ