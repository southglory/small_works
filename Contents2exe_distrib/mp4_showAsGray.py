import time

from cv2 import cvtColor, COLOR_RGB2GRAY, COLOR_GRAY2RGB
import os

os.environ["IMAGEIO_FFMPEG_EXE"] = 'ffmpeg.exe'
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from moviepy.video.io.preview import  preview
import pygame

#works without the .exe also
pygame.init()

pygame.display.set_caption('Show Video on screen')

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
time.sleep(1)

clips = ImageSequenceClip(new_frames, fps = fps, durations = duration)
#
preview(clips)

# clips.write_videofile("contents/videos/video_gray.mp4")
pygame.quit()

