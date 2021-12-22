-----------------------------------------------------------------------------
"exe 파일로 distribution"하는 법을 익히기 위한 연습 프로젝트.
-----------------------------------------------------------------------------

fixed bug : 

1.pyinstaller로 exe를 만들때 ffmpeg가 번들되지 않는 문제

해결방법 : 

moviepy를 import하기 전에, os.environ["IMAGEIO_FFMPEG_EXE"] = 'ffmpeg.exe' 선언

주의점 : 

r'D:\Users\yk_home\anaconda3\envs\imgWork\Library\bin\ffmpeg.exe'

library경로에 있는 ffmpeg는 300kB 정도 밖에 안하는 반쪽짜리이므로, 손쉽게 exe만 가지고 실행하고 싶다면
ffmpeg 공식 홈페이지에서 Essencial download를 하고 약 70MB가량의 ffmpeg.exe를 사용해야 한다..
ffmpeg.7z의 압축을 해제해서 사용하면 됨.

2. exe를 실행할 때 moviepy의 audio 등을 찾을 수 없는 문제

해결방법:

moviepy의 각 플러그인을 따로 import함.

3. ffmpeg.exe가 프로그램 my.exe와 같은 경로에 없어도 my.exe가 잘 실행되도록 하는 방법

pyinstaller로 exe를 만들어 줄때 --add-data "ffmpeg.exe;." 명령어를 포함한다.

*_____________________________________________________________*

pyinstaller mp4_showAsGray.py --noconsole -F --add-data "ffmpeg.exe;."
(이 경우 ffmpeg.exe는 70MB파일).

pyinstaller mp4_Convert2Gray.py --noconsole -F --add-data "ffmpeg.exe;."
pyinstaller mp4_Save30frames_jpg.py --noconsole -F --add-data "ffmpeg.exe;."
pyinstaller mp4_SaveAllframes_jpg.py --noconsole -F --add-data "ffmpeg.exe;."
pyinstaller mp4_getVideoINFOtxt.py --noconsole -F


*----------------------------------------------------------*
video 출처 :
픽사베이 moshehar/110 videos
<a href="https://pixabay.com/ko/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=15305">Pixabay</a>에서 <a href="https://pixabay.com/ko/users/moshehar-7046690/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=62487">Moshe Harosh</a> 님이 제공한 동영상


<img width="249" alt="dogs" src="https://user-images.githubusercontent.com/51065570/135828805-e9fe9f97-565a-469a-94a3-5b7f4a19fcdb.PNG">
