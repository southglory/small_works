import os
os.environ["IMAGEIO_FFMPEG_EXE"] = 'ffmpeg.exe'
from moviepy.video.io.VideoFileClip import VideoFileClip
from datetime import datetime as time
from createFolder import createFolder

my_clip = VideoFileClip("contents/videos/video.mp4")

duration = my_clip.duration
fps = my_clip.fps
# frames = int(fps * duration)
# n_frames = my_clip.reader.nframes
print("g")
i=0.0
frame = 0


now = time.now()
foldername = str(now.day)+str(now.hour)+str(now.minute)
dir = createFolder("contents/picture/"+foldername)

n_frames=30
while frame <=n_frames:
    my_clip.save_frame(dir + '/' + str(frame) + ".jpg", i)
    i += duration/n_frames
    frame += 1
