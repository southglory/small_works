from cv2 import VideoCapture, CAP_PROP_FPS, CAP_PROP_FRAME_COUNT

cap = VideoCapture("contents/videos/video.mp4")
fps = cap.get(CAP_PROP_FPS)      # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
frame_count = int(cap.get(CAP_PROP_FRAME_COUNT))
duration = frame_count/fps

with open("contents/videos/videoInfo.txt", 'w') as f:
    f.write('fps = ' + str(fps)+'\n')
    f.write('number of frames = ' + str(frame_count)+'\n')
    f.write('duration (S) = ' + str(duration)+'\n')
    minutes = int(duration / 60)
    seconds = duration % 60
    f.write('duration (M:S) = ' + str(minutes) + ':' + str(seconds)+'\n')

cap.release()

