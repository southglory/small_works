import os
import time

from cv2 import cvtColor, COLOR_RGB2GRAY, COLOR_GRAY2RGB
os.environ["IMAGEIO_FFMPEG_EXE"] = 'ffmpeg.exe'
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from  pygame import init,display, quit
from createFolder import createFolder
from datetime import datetime as time
from time import sleep
init()

display.set_caption('Show Video on screen')

video = VideoFileClip('contents/videos/video.mp4')

duration = video.duration
fps = video.fps
count =1
gray_frames = []

def gray(image):
    """Flips an image vertically """
    gray = cvtColor(image, COLOR_RGB2GRAY)
    rgb= cvtColor(gray,COLOR_GRAY2RGB)
    return rgb # remember that image is a numpy array

new_frames = [ gray(frame) for frame in video.iter_frames()]
sleep(1)

clips = ImageSequenceClip(new_frames, fps = fps, durations = duration)
#
# clips.preview()

now = time.now()
foldername = str(now.day)+str(now.hour)+str(now.minute)
dir = createFolder("contents/videos/"+foldername)

clips.write_videofile(dir+"/video_gray.mp4")
quit()

